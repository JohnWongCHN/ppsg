import click
import os
import pkg_resources
from jinja2 import Environment, PackageLoader, select_autoescape

class Core():
    """ main class """
    def __init__(self, name, desc, author, email):
        self.project_name = name
        self.project_desc = desc
        self.project_author = author
        self.author_email = email
        self.project_path = os.path.join(os.getcwd(), name)
        self.package_path = os.path.join(self.project_path, name)
        self.docs_path = os.path.join(self.project_path, 'docs')
        self.test_path = os.path.join(self.project_path, 'tests')
        self.env = Environment(
            loader=PackageLoader('ppsg', 'templates'),
            autoescape=select_autoescape(['html', 'xml'])
        )

    def gen_dir(self):
        """
        生成项目目录结构, structure like below
        project_name/
            project_name/
                __init__.py
                ...source code files...
            tests/
                __init__.py
                ...unit test files...
            docs/
                ...documentation files...
        """
        try:
            os.makedirs(self.package_path)
            os.makedirs(self.docs_path)
            os.makedirs(self.test_path)
        except Exception as e:
            click.echo(str(e))

    def gen_changelog_file(self):
        """        
        生成changelog.md文件
        """
        try:
            # 使用jinja的packageloader加载位于包里的模版文件
            changelog_template = self.env.get_template('CHANGELOG.jinja2')
            # 直接使用stream方法然后dump出来
            changelog_template.stream({'project': self.project_name}).dump(os.path.join(self.project_path, 'CHANGELOG.md'))
        except Exception as e:
            print('Exception output: ' + str(e))

    def gen_license_file(self):
        """
        生成license文件
        """
        try:
            # 使用jinja的packageloader加载位于包里的模版文件
            license_template = self.env.get_template('LICENSE.jinja2')
            # 直接使用stream方法然后dump出来
            license_template.stream().dump(os.path.join(self.project_path, 'LICENSE'))
        except Exception as e:
            print('Exception output: ' + str(e))

    def gen_setup_file(self):
        """
        生成setup.py文件
        """
        try:
            # 使用jinja的packageloader加载位于包里的模版文件
            setup_template = self.env.get_template('setup.jinja2')
            # 直接使用stream方法然后dump出来
            setup_template.stream({'project': self.project_name,
                                   'desc': self.project_desc,
                                   'author': self.project_author, 
                                   'email': self.author_email}).dump(os.path.join(self.project_path, 'setup.py'))
        except Exception as e:
            print('Exception output: ' + str(e))

    def gen_readme_file(self):
        """
        生成readme.md文件
        """
        try:
            # 使用jinja的packageloader加载位于包里的模版文件
            readme_template = self.env.get_template('README.jinja2')
            # 直接使用stream方法然后dump出来
            readme_template.stream({'project': self.project_name}).dump(os.path.join(self.project_path, 'README.md'))
        except Exception as e:
            print('Exception output: ' + str(e))

    def gen_requirement_file(self):
        """
        生成requirement.txt文件
        """
        try:
            # 使用jinja的packageloader加载位于包里的模版文件
            requirement_template = self.env.get_template('requirement.jinja2')
            # 直接使用stream方法然后dump出来
            requirement_template.stream().dump(os.path.join(self.project_path, 'requirement.txt'))
        except Exception as e:
            print('Exception output: ' + str(e))

    def gen_requirement_dev_file(self):
        """ 
        生成requirement-dev.txt文件
        """
        try:
            # 使用jinja的packageloader加载位于包里的模版文件
            requirement_dev_template = self.env.get_template('requirement-dev.jinja2')
            # 直接使用stream方法然后dump出来
            requirement_dev_template.stream().dump(os.path.join(self.project_path, 'requirement-dev.txt'))
        except Exception as e:
            print('Exception output: ' + str(e))
    
    def gen_gitignore_file(self):
        """ 
        生成gitignore文件
        """
        try:
            # 使用jinja的packageloader加载位于包里的模版文件
            gitignore_template = self.env.get_template('gitignore.jinja2')
            # 直接使用stream方法然后dump出来
            gitignore_template.stream().dump(os.path.join(self.project_path, '.gitignore'))
        except Exception as e:
            print('Exception output: ' + str(e))
        
    def gen_MANIFEST_file(self):
        """
        生成MANIFEST.in文件
        """
        try:
            # 使用jinja的packageloader加载位于包里的模版文件
            manifest_template = self.env.get_template('MANIFEST.jinja2')
            # 直接使用stream方法然后dump出来
            manifest_template.stream().dump(os.path.join(self.project_path, 'MANIFEST.in'))
        except Exception as e:
            print('Exception output: ' + str(e))

@click.command()
@click.option('-n', '--name', required=True, prompt=True, help='项目名')
@click.option('-d', '--desc', help='项目介绍', prompt=True, default='demo project')
@click.option('-a', '--author', help='项目作者', prompt=True, default='John Wong')
@click.option('-m', '--email', help='作者邮箱', prompt=True, default='john-wong@outlook.com')
def main(name, desc, author, email):
    """
    main
    """
    project = Core(name=name, desc=desc, author=author, email=email)
    project.gen_dir()
    project.gen_changelog_file()
    project.gen_license_file()
    project.gen_setup_file()
    project.gen_readme_file()
    project.gen_requirement_file()
    project.gen_requirement_dev_file()
    project.gen_gitignore_file()
    project.gen_MANIFEST_file()
    print('{}项目结构已创建!'.format(name))