# Run Instructions

## python daemon code
```
import os
def process():
    print(f"Hello {datetime.datetime.now()}", flush=True)

print(os.getenv('mypass', None))
print(os.getenv('mongoConnectionString', None))

while True:
    process()
    time.sleep(20)
```

## Build Docker image

```
docker build -t pydaemon:dev2 .
```

## Deploy image to kubernetes cluster

```
kubectl apply -f deploy.yaml
```

## Expected logs
```
topsecret
mongodb://mongo-ms-md:27017
Hello 2019-07-19 01:24:48.415305
Hello 2019-07-19 01:25:08.433002
```