# Flask Application

If you are on Mac OS X or Linux, chances are that one of the following two commands will work for you:

```
$ sudo easy_install virtualenv
```

or even better:

```
$ sudo pip install virtualenv
```

One of these will probably install virtualenv on your system. Maybe it’s even in your package manager. If you use Ubuntu, try:

```
$ sudo apt-get install python-virtualenv
```

If you are on Windows and don’t have the easy_install command, you must install it first. Check the pip and distribute on Windows section for more information about how to do that. Once you have it installed, run the same commands as above, but without the sudo prefix.

Once you have virtualenv installed, just fire up a shell and create your own environment. I usually create a project folder and a venv folder within:

```
$ mkdir myproject
$ cd myproject
$ virtualenv venv
New python executable in venv/bin/python
Installing distribute............done.
```

Now, whenever you want to work on a project, you only have to activate the corresponding environment. On OS X and Linux, do the following:

```
$ . venv/bin/activate
```

If you are a Windows user, the following command is for you:

```
$ venv\scripts\activate
```

Either way, you should now be using your virtualenv (notice how the prompt of your shell has changed to show the active environment).

Now you can just enter the following command to get Flask activated in your virtualenv:

```
$ pip install Flask
```

A few seconds later and you are good to go.

System-Wide Installation
This is possible as well, though I do not recommend it. Just run pip with root privileges:

```
$ sudo pip install Flask
```

(On Windows systems, run it in a command-prompt window with administrator privileges, and leave out sudo.)

Living on the Edge
If you want to work with the latest version of Flask, there are two ways: you can either let pip pull in the development version, or you can tell it to operate on a git checkout. Either way, virtualenv is recommended.

Get the git checkout in a new virtualenv and run in development mode:

```
$ git clone http://github.com/mitsuhiko/flask.git
Initialized empty Git repository in ~/dev/flask/.git/
$ cd flask
$ virtualenv venv --distribute
New python executable in venv/bin/python
Installing distribute............done.
$ . venv/bin/activate
$ python setup.py develop
...
Finished processing dependencies for Flask
```

This will pull in the dependencies and activate the git head as the current version inside the virtualenv. Then all you have to do is run git pull origin to update to the latest version.

To just get the development version without git, do this instead:

```
$ mkdir flask
$ cd flask
$ virtualenv venv --distribute
$ . venv/bin/activate
New python executable in venv/bin/python
Installing distribute............done.
$ pip install Flask==dev
...
Finished processing dependencies for Flask==dev
```

pip and distribute on Windows
On Windows, installation of easy_install is a little bit trickier, but still quite easy. The easiest way to do it is to download the distribute_setup.py file and run it. The easiest way to run the file is to open your downloads folder and double-click on the file.

Next, add the easy_install command and other Python scripts to the command search path, by adding your Python installation’s Scripts folder to the PATH environment variable. To do that, right-click on the “Computer” icon on the Desktop or in the Start menu, and choose “Properties”. Then click on “Advanced System settings” (in Windows XP, click on the “Advanced” tab instead). Then click on the “Environment variables” button. Finally, double-click on the “Path” variable in the “System variables” section, and add the path of your Python interpreter’s Scripts folder. Be sure to delimit it from existing values with a semicolon. Assuming you are using Python 2.7 on the default path, add the following value:

;C:\Python27\Scripts
And you are done! To check that it worked, open the Command Prompt and execute easy_install. If you have User Account Control enabled on Windows Vista or Windows 7, it should prompt you for administrator privileges.

Now that you have easy_install, you can use it to install pip:

```
> easy_install pip
```
