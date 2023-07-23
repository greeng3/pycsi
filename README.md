# pycsi
Tools for analysis of python code

## Publishing

- poetry config pypi-token.pypi your-api-token
- poetry build
- poetry publish
  - Publishing pycsi (0.1.0) to PyPI
  - Uploading pycsi-0.1.0-py3-none-any.whl FAILED
  -
  - HTTP Error 403: Invalid or non-existent authentication information. See https://pypi.org/help/#invalid-auth for more information. | b'<html>\n <head>\n  <title>403 Invalid or non-existent authentication information. See https://pypi.org/help/#invalid-auth for more information.\n \n <body>\n  <h1>403 Invalid or non-existent authentication information. See https://pypi.org/help/#invalid-auth for more information.\n  Access was denied to this resource.<br/><br/>\nInvalid or non-existent authentication information. See https://pypi.org/help/#invalid-auth for more information.\n\n\n \n'

### Another failure, trying to use a Trusted Publisher
git --no-optional-locks -c color.branch=false -c color.diff=false -c color.status=false -c diff.mnemonicprefix=false -c core.quotepath=false -c credential.helper=sourcetree push -v --tags origin refs/heads/poetry-publishing:refs/heads/poetry-publishing 
Pushing to https://github.com/greeng3/pycsi.git
POST git-receive-pack (2035 bytes)
To https://github.com/greeng3/pycsi.git
 ! [remote rejected] poetry-publishing -> poetry-publishing (refusing to allow an OAuth App to create or update workflow `.github/workflows/publish.yml` without `workflow` scope)
error: failed to push some refs to 'https://github.com/greeng3/pycsi.git'
Completed with errors, see above