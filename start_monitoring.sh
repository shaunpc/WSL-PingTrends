
# Start the KAFKA zookeeper process in the background
su kafka $KAFKA_HOME/bin/zookeeper-server-start.sh $KAFKA_HOME/config/zookeeper.properties &

# Start the KAFKA broker process in the background
su kafka $KAFKA_HOME/bin/kafka-server-start.sh $KAFKA_HOME/config/server.properties &

# 