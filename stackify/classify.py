from typing import List, Optional


HIDE_TAGS = ["none", "ios", "machine-learning", "azure", "mongodb", "sql-server", "web", "java", "fsharp",
             "clojure", "business-intelligence", "kafka", "ansible"]

MACHINE_LEARNING_TAGS = ["machine-learning", "anaconda", "tensorflow", "nltk", "pandas", "classification", "keras",
                         "numpy", "pytorch", "classification", "adaboost", "matplotlib", "scikit-learn",
                         "deep-learning", "tensorflow2.0", "jupyter-notebook", "nlp",
                         "reinforcement-learning", "dataframe", "jupyter", "seaborn", "neural-network"]
AZURE_TAGS = ["azure", "azure-functions", "azure-data-studio", "azureservicebus", "azure-devops", "azure-web-sites",
              "azure-storage", "azure-data-factory", "azure-cosmosdb", "azure-notificationhub", "azure-keyvault",
              "azure-sql-database", "azure-security", "azure-cli", "azure-api-management", "azure-eventhub",
              "azure-data-lake", "azure-machine-learning-studio", "azure-web-app-service", "azure-application-insight",
              "azure-logic-apps", "azure-active-directory", "azure-storage-blobs", "azure-blob-storage"]
JAVA_TAGS = ["spring", "spring-boot", "java", "java-8", "tomcat", "spring-webflux", "maven", "jakarta-ee",
             "spring-batch", "spring-security", "spring-mvc", "tomcat7", "rx-java", "java-7", "spring-data-jpa",
             "spring-boot-activator", "spring-data-redis", "spring-data"]
ARCHITECTURE_TAGS = ["oop", "software-design", "architecture", "microservices", "distributed-system"]
C_TAGS = ["c", "c++", "gcc", "c++11", "c++14"]
IOS_TAGS = ["swift", "xcode", "swiftui", "ios", "swift3", "swift4", "combine", "swift5", "apple-watch"]
LINUX_TAGS = ["linux", "unix", "linux-kernel", "debian"]
PYTHON_TAGS = ["python", "python-3.x", "python-3.8", "python-2.7", "pytest", "python-3.6", "python-3.7"]
WEB_TAGS = ["css", "html", "html5-canvas", "bootstrap-4", "bootstrap-datepicker"]
ALGO_TAGS = ["algorithm", "time-complexity", "heapsort", "binary-tree"]
JETBRAINS_TAGS = ["intellij-idea", "webstorm", "pycharm", "clion"]
SECURITY_TASG = ["security", "malware"]
NETWORKING_TASG = ["networking", "ssh", "wireshark"]
KAFKA_TAGS = ["apache-kafka"]

FIRST_LEVEL_RULES = [
    {"site": "stackoverflow", "include": ",".join(JETBRAINS_TAGS), "result": "intellij"},
    {"site": "stackoverflow", "include": "github-actions", "result": "github"},
    {"site": "stackoverflow", "include": "vim", "result": "vim"},
    {"site": "stackoverflow", "include": "ansible", "result": "ansible"},
    {"site": "stackoverflow", "include": "clickhouse", "result": "clickhouse"},
    {"site": "stackoverflow", "include": "redis", "result": "redis"},
    {"site": "stackoverflow", "include": "prometheus", "result": "prometheus"},
    {"site": "stackoverflow", "include": "elasticsearch", "result": "elasticsearch"},
    {"site": "stackoverflow", "include": "cassandra", "result": "cassandra"},
    {"site": "stackoverflow", "include": ",".join(KAFKA_TAGS), "result": "kafka"},
    {"site": "stackoverflow", "include": "rabbitmq", "result": "rabbitmq"},
    {"site": "stackoverflow", "include": "unit-testing", "result": "unit testing"},
    {"site": "stackoverflow", "include": ",".join(ARCHITECTURE_TAGS), "result": "architecture"},
    {"site": "stackoverflow", "include": ",".join(MACHINE_LEARNING_TAGS), "result": "machine-learning"},
    {"site": "stackoverflow", "include": ",".join(AZURE_TAGS), "result": "azure"},
    {"site": "stackoverflow", "include": "f#", "result": "fsharp"},
    {"site": "stackoverflow", "include": "clojure", "result": "clojure"},
    {"site": "stackoverflow", "include": "git", "result": "git"},
    {"site": "stackoverflow", "include": "github", "result": "git"},
    {"site": "stackoverflow", "include": "kubernetes", "result": "kubernetes"},
    {"site": "stackoverflow", "include": "docker", "result": "docker"},
    {"site": "stackoverflow", "include": "sql-server", "result": "sql-server"},
    {"site": "stackoverflow", "include": "bash", "result": "bash"},
    {"site": "stackoverflow", "include": "sed", "result": "bash"},
    {"site": "stackoverflow", "include": "awk", "result": "bash"},
    {"site": "stackoverflow", "include": ",".join(JAVA_TAGS), "result": "java"},
    {"site": "stackoverflow", "include": ",".join(IOS_TAGS), "result": "ios"},
    {"site": "stackoverflow", "include": "go", "result": "go"},
    {"site": "stackoverflow", "include": ",".join(C_TAGS), "result": "c"},
    {"site": "stackoverflow", "include": "powerbi", "result": "business-intelligence"},
    {"site": "stackoverflow", "include": ",".join(PYTHON_TAGS), "result": "python"},
    {"site": "stackoverflow", "include": "postgresql", "result": "postgresql"},
    {"site": "stackoverflow", "include": "mongodb", "result": "mongodb"},
    {"site": "stackoverflow", "include": ",".join(LINUX_TAGS), "result": "linux"},
    {"site": "stackoverflow", "include": ",".join(WEB_TAGS), "result": "web"},
    {"site": "stackoverflow", "include": ",".join(NETWORKING_TASG), "result": "networking"},
    {"site": "stackoverflow", "include": ",".join(ALGO_TAGS), "result": "algorithm"},
    {"site": "stackoverflow", "include": ",".join(SECURITY_TASG), "result": "security"},
    {"site": "stackoverflow", "include": "macos", "result": "macos"},
    {"site": "stackoverflow", "include": "markdown", "result": "markdown"},
    {"site": "stackoverflow", "include": "grafana", "result": "grafana"},
    {"site": "stackoverflow", "include": "nginx", "result": "nginx"},

    {"site": "codereview", "include": "python", "result": "cr: python"},
    {"site": "codereview", "include": "c++", "result": "cr: c++"},
    {"site": "codereview", "include": "go", "result": "cr: go"},

    {"site": "askdifferent", "include": "*", "result": "s: apple"},
]

SECOND_LEVEL_RULES = [
    {"site": "stackoverflow", "first": "big data", "include": "cassandra", "result": "cassandra"},
    {"site": "stackoverflow", "first": "big data", "include": "apache-kafka", "result": "kafka"},
]


class Classifier:
    def __init__(self, stop_tags, first_level_rules):
        self.stop_tags = stop_tags
        self.first_level_rules = first_level_rules

    def has_stop_tag(self, tags: List[str]) -> bool:
        for tag in tags:
            if tag in self.stop_tags:
                return True
        return False

    def first_level_classification(self, tags: List[str], site: str) -> Optional[str]:
        for rule in self.first_level_rules:
            if rule["site"] == site and rule["include"] == "*":
                return rule["result"]
            elif rule["site"] == site:
                for rule_tag in rule["include"].split(","):
                    if rule_tag in tags:
                        return rule["result"]
        return "none"

    def second_level_classification(self, tags: List[str], first: str) -> Optional[str]:
        for rule in SECOND_LEVEL_RULES:
            if rule["first"] == first and rule["include"] in tags:
                return rule["result"]

        return "none"

    def classify(self, questions: List) -> List:
        result = []
        for q in questions:
            if not self.has_stop_tag(q["tags"]):
                q["first"] = self.first_level_classification(q["tags"], q["site"])
                q["second"] = self.second_level_classification(q["tags"], q["first"])
                q["category"] = q["first"]
                q["subcategory"] = q["second"]
                result.append(q)
        return result
