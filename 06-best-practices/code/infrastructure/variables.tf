variable "aws_region" {
    description = "AWS region to create resources"
    default = "eu-west-1"
}

variable "project_id" {
    description = "project_id"
    default = "mlops-zoomcamp"
}

variable "source_stream_name" {
    description = "kinesis source stream name"
}