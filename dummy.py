print("hello world")
print("more shit")

#You may also need to update the origin for your repository if it is set to HTTPS. Do this to switch to SSH:
'''
git remote -v
git remote set-url origin git@github.com:USERNAME/REPONAME.git
mkdir -p $HOME/.ssh
chmod 0700 $HOME/.ssh
ssh-keygen
ssh-copy-id -i [ssh-key-location] [username]@[server-ip-address]
cat ~/.ssh/id_rsa.pub







'''
