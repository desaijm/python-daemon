# Run Instructions

## Python daemon code
```
import os
def process():
    print(f"Hello {datetime.datetime.now()}", flush=True)

print("mypass = " + os.getenv('mypass', "notfound"))
print("mongoConnectionString = " + os.getenv('mongoConnectionString', "notfound"))

while True:
    process()
    time.sleep(20)
```

## Run code locally on windows environment.

### Setup environments in windows os

- Search for "edit environment variables"
- Add following two environment variables
    - name = mypass, value = secretfromwindows
    - name = mongoConnectionString, value = connectionStringFromWindows

![add variables](/docs/AddWindowsEnvironmentVariables.png)

## Run code in kubernetes

### 1. Build Docker image

#### Dockerfile
```
FROM python:3.6
ADD main.py /
CMD [ "python", "./main.py" ]
```
#### Build commands
```
docker build -t pydaemon:dev2 .
```

#### Expected logs locally
```
mypass = secretfromwindows
mongoConnectionString = connectionStringFromWindows
Hello 2019-07-19 08:23:30.835177
Hello 2019-07-19 08:23:50.835859
```

### 2. Deploy image to kubernetes cluster

#### Deploy yaml file
```
apiVersion: apps/v1beta1
kind: Deployment
metadata:
  name: py-daemon
spec:
  replicas: 1
  template:
    metadata:
      labels:
        app: py-daemo
    spec:
      containers:
      - name: py-daemo
        image: pydaemon:dev2
        imagePullPolicy: Never
        env:
        - name: mypass
          value: topsecret
        - name: mongoConnectionString
          value: mongodb://mongo-ms-md:27017
```
#### Build commands
```
kubectl apply -f deploy.yaml
```

#### Expected logs in kubernetes
```
mypass = topsecret
mongoConnectionString = mongodb://mongo-ms-md:27017
Hello 2019-07-19 08:23:30.835177
Hello 2019-07-19 08:23:50.835859
```
