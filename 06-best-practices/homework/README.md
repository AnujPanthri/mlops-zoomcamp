## start localstack with s3 service
```bash
docker compose up -d
```

## configure environment variable
```bash
export AWS_ENDPOINT_URL=http://localhost:4566
aws s3 ls
```

## make s3 Bucket
```bash
aws s3 mb s3://nyc-duration
```

## Unit tests
```bash
pytest tests/
```

## Integration tests
```bash
./integration_test/run.sh
```