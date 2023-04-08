# webapptemplate
fully dockerized (using podman) django web app

# features
- login
- user profiles
- (large) file upload
- zipped/non-zipped file download
- task queue (using django_rq)
- dockerization using podman
- nginx proxy

# comments
webapp should be fully testable without podman. if you need gpu support, obviously you
need hardware that can do this. or you set it up such that you can run gpup calculations
in cpu-mode using abstraction.