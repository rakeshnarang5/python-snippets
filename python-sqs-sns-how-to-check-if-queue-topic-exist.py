
    if args.dry_run:
        logging.info("Running a dry run")
        topicExists = False
        try:
            response = sns_client.get_topic_attributes(
                TopicArn= get_topic_arn("my_stupid_topic", args.region, aws_account_id)
            )
            if response is not None:
                topicExists = True
        except Exception as e:
            print("does not exists")

        if(topicExists):
            print("topic exists")
        else:
            print("topic does not exist")


        logging.info("i want to check queue now")
        jelineQueueExists = False
        try:
            response = sqs_client.get_queue_url(QueueName = "terra----jetline-completion-message-queue")
            if response is not None:
                jelineQueueExists = True
                print(response)
        except Exception as e:
            print(" jeline queue does not exists")

        if(jelineQueueExists):
            logging.info("jeline queue exists")
        else:
            logging.info("jeline queue does not exist")
