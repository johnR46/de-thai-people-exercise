FROM bitnami/spark:3.5
USER root
RUN install_packages curl
USER 1001
RUN curl https://repo1.maven.org/maven2/software/amazon/awssdk/s3/2.23.12/s3-2.23.12.jar --output /opt/bitnami/spark/jars/s3-2.23.12.jar
RUN curl https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk/1.12.646/aws-java-sdk-1.12.646.jar --output /opt/bitnami/spark/jars/aws-java-sdk-1.12.646.jar
USER spark