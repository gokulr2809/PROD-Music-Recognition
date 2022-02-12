from codecs import utf_16_be_encode
from github import Github
g = Github('github api key')

def gitupload(z):
    repo = g.get_user().get_repo('store')
    all_files = []
    contents = repo.get_contents("")
    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path))
        else:
            file = file_content
            all_files.append(str(file).replace('ContentFile(path="','').replace('")',''))
    filez_name = r"Samples\ "+z+'.m4a'
    with open(filez_name,'rb') as file:
        content = file.read()

    # Upload to github
    y=z+'.m4a'
    git_file = y
    repo.create_file(git_file, "committing files", content, branch="main")
    print('uploaded')