terraform {
    required_version = ">= 1.0"
}

provider "aws" {
    region = var.aws_region
}

data "aws_caller_identity" "current_identity" {}

locals {
    account_id = data.aws_caller_identity.current_identity.account_id
}

# ride events
module "source_kinesis_stream" {
    source = "./modules/kinesis"
    stream_name = "${var.source_stream_name}_${var.project_id}"
    tags = var.project_id
    shard_count = 2
    retention_period = 48
}