# Kafka_Challenge
Dieses Projekt bietet eine einfache Lösung zum Verfolgen von Änderungen (Edits) auf Wikipedia-Seiten mithilfe von Apache Kafka. Es besteht aus einem Producer und einem Consumer für Kafka-Nachrichten.

# Voraussetzungen

Bevor Sie dieses Projekt verwenden können, müssen Sie sicherstellen, dass Sie die folgenden Voraussetzungen erfüllen:

Docker ist installiert und ausgeführt.
Sie haben Python installiert und die erforerlichen Bibliotheken installiert und importiert
- Pandas
- Kafka

# Projektstruktur

Die Projektstruktur besteht aus den folgenden Hauptkomponenten:

producer.py: Ein Python-Skript, das Nachrichten aus der CSV-Datei liest und sie als Kafka-Nachrichten an ein Kafka-Topic sendet.
consumer.py: Ein Python-Skript, das Kafka-Nachrichten vom Kafka-Topic abonniert, die Edits auf Wikipedia-Seiten darstellen, und die Anzahl der Edits pro Minute sowohl global als auch für die deutsche Wikipedia verfolgt.
docker-compose.yaml: Eine Docker Compose-Datei zur Konfiguration eines Kafka-Brokers und eines Zookeepers.

# Docker Compose Setup

Dieses Docker Compose-Setup enthält zwei Container, `kafka` und `zookeeper`, die für die Kafka-Challenge verwendet werden. In diesem README-Dokument finden Sie Informationen zur Konfiguration und Verwendung dieser Container.



### Details
- **Image**: confluentinc/cp-kafka:latest
- **Container-Name**: kafka-challenge-kafka-1
- **Verfügbare Ports**: 9092 (Kafka-Port)

### Konfiguration
- `KAFKA_ADVERTISED_LISTENERS`: Der beworbene Listener für Kafka. Hier ist die Konfiguration auf `PLAINTEXT://kafka-challenge-kafka-1:9092` festgelegt.
- `KAFKA_ZOOKEEPER_CONNECT`: Die Verbindung zum ZooKeeper-Container. Hier ist die Konfiguration auf `zookeeper:2181` festgelegt.

### Verwendung
- Der Kafka-Container dient dazu, Kafka-Broker-Funktionalität bereitzustellen.
- Die Kafka-Broker-Instanz kann auf Port 9092 erreicht werden.

## ZooKeeper-Container (`zookeeper`)

### Details
- **Image**: confluentinc/cp-zookeeper:latest
- **Container-Name**: kafka-challenge-zookeeper-1
- **Verfügbare Ports**: 2181 (ZooKeeper-Port)

### Konfiguration
- `ZOOKEEPER_CLIENT_PORT`: Der Client-Port für ZooKeeper. Hier ist die Konfiguration auf `2181` festgelegt.

### Verwendung
- Der ZooKeeper-Container wird für die Koordination und Verwaltung des Kafka-Clusters verwendet.
- Die ZooKeeper-Instanz kann auf Port 2181 erreicht werden.

## Verwendung des Docker-Compose-Setups

1. Stellen Sie sicher, dass Docker und Docker Compose auf Ihrem System installiert sind.

2. Navigieren Sie im Terminal zum Verzeichnis, in dem sich die `docker-compose.yml`-Datei befindet.

3. Führen Sie den Befehl `docker-compose up` aus, um die Container zu starten.

4. Sie können die Container beenden, indem Sie `docker-down` ausführen.

5. Überprüfen Sie den Stand der Container mit dem Command `docker ps`

