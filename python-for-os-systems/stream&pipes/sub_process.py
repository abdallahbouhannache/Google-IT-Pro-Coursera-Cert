import subprocess as sb

rs=sb.run(['ls'],['-la'])
print(rs)

hostres=sb.run(['host','8.8.8.8'],capture_output=True)
print(hostres.returncode)
print(hostres.stdout)
print(hostres.stdout.decode.split())

resexist=sb.run(['rm','am_not_here.txt'],capture_output=True)
print(resexist.stdout)
print(resexist.stderr)

## adding environement variable to sb
my_env=os.environ.copy()
my_env['PATH']=os.path.join('/opt/myapp/',my_env['PATH'])

resENV=sb.run(['myapp'],env=my_env)

print(resENV)