# Run tests locally

Build Docker image to run test cases

`docker build -t pass-client-lib-unittest .`

Once image is build, run tests

`docker run -it pass-client-lib-unittest /bin/bash -c 'sh run_tests.sh'`