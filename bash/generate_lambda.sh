
# start with all python files
zip -r9 build/lambda.zip py/

# add the temp folder for downloads
zip -g9 build/lambda.zip temp/README.md

# add all the dependencies
cd venv_lambda/lib/python3.6/site-packages/
zip -gr9 ../../../../build/lambda.zip *
cd ../../../../
