from subprocess import getoutput
from sys import argv

if len(argv) < 2:
    print('A mensagem de commit é requerida.')
    exit(0)

commit_message = argv[1].replace('"', '')
retry_if_failed = False

if argv[2] and argv[2].isnumeric():
    retry_if_failed = True

cmd_add = 'git add .'
cmd_commit = 'git commit -m "{}"'.format(commit_message)
cmd_push_heroku = 'git push heroku master --force'
cmd_push_github = 'git push -u origin master'

def heroku_push():
    print(cmd_push_heroku)
    heroku_output = getoutput(cmd_push_heroku)
    print(heroku_output)
    if 'time out' in heroku_output \
            or 'fail' in heroku_output \
            or 'error' in heroku_output:
        return False
    return True

def github_push():
    print(cmd_push_github)
    github_output = getoutput(cmd_push_github)
    print(github_output)

    if 'time out' in github_output \
            or 'fail' in github_output \
            or 'error' in github_output:
        return False
    return True

print(cmd_add)
getoutput(cmd_add)

print(cmd_commit)
getoutput(cmd_commit)

if retry_if_failed:
    while not heroku_push():
        continue

    while not github_push():
        continue
else:
    heroku_push()
    github_push()