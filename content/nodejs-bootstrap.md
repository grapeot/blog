Title: Self-Updating Node.js Web App
Date: 2013-11-25 18:17
Category: Computing 
Tags: nodejs, English
Slug: self-updating-nodejs-web-app

Can a node.js/express.js web app update itself from a github repo? (i.e. whenever we do a `git push` to github, the server side will also use `git pull` to update itself)

It's possible thanks to the powerful WebHook of github.

The basic idea is, to use a separate light-weight "app" to listen to a different address, and trigger the `git pull` and the restart work whenever github visits the url.
It's nearly trivial given the express.js framework.
The core code is shown below.
Note we use `child_process.spawn()` to control the life cycle of the child process.

    :::javascript
    function restartApp(req, res)
    {
        spawn('git', ['pull']);
        child.kill();
        startApp();
        res.send('ok.');
    }

    function startApp()
    {
        child = spawn('node', ['app.js']);
        child.stdout.setEncoding('utf8');
        child.stdout.on('data', function (data) {
            var str = data.toString()
            console.log(str);
        });
        child.on('close', function (code) {
            console.log('process exit code ' + code);
        });
    }

The complete code with context is put [here](https://github.com/grapeot/learn-expressjs/blob/master/bootstrap.js).
To launch the program, `nohup node ./bootstrap.js &` is a good idea which is able to solve the `zsh` background job problem.

[Another](https://yage.ai/adding-a-delay-to-ifttt-recipes.html) lightweight way to implement WebHook isn't it?