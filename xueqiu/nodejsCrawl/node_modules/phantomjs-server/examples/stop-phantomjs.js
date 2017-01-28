require('child_process').exec(process.platform === 'win32' ? 'taskkill /F /IM phantomjs.exe /T' : 'killall phantomjs',
  function (error, stdout, stderr) {
      console.log(stdout);
  });
