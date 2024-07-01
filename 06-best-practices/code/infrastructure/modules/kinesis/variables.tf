variable "stream_name" {
    type = string
    description = "stream name for kinesis"
}

variable "shard_count" {
    type = number
    description = "shard count"
}

variable "retention_period" {
    type = number
    description = "kinesis stream data retention_period"
}

variable "shard_level_metrics" {
    type        = list(string)
    description = "shard_level_metrics"
    default     = [
    "IncomingBytes",
    "OutgoingBytes",
    "OutgoingRecords",
    "ReadProvisionedThroughputExceeded",
    "WriteProvisionedThroughputExceeded",
    "IncomingRecords",
    "IteratorAgeMilliseconds",
  ]
}

variable "tags" {
    type = string
    description = "Tags for kinesis stream"
}