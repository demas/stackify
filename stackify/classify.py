from typing import List, Optional

PHP_TAGS = ["php", "laravel", "joomla", "cakephp", "wordpress", "symfony", "laravel-5.1", "laravel-5", "typo3",
            "laravel-6", "drupal-8", "php-curl", "typo3-8.x", "codeigniter", "drupal", "yii2", "odoo-12",
            "laravel-7", "magento", "magento-2.3", "lavarel-5.7", "magento2", "drupal-7", "symfony-3.4",
            "odoo-13", "typo3-9.x", "php-7.4", "symfony4", "umbraco", "yii", "composer-php", "phpexcel",
            "zend-framework", "phpspreadsheet"]
JS_TAGS = ["javascript", "knockout.js", "d3.js", "ember.js", "three.js", "backbone.js", "angular3", "angular4",
           "angular5", "mocha", "chai", "webpack", "eslint", "redux", "underscore.js", "vue.js", "vuejs2", "svelve",
           "angularjs", "reactjs", "node.js", "handlebars.js", "extjs", "gruntjs", "express", "mongoose", "angular8",
           "angular9", "koa", "fabricjs", "angular-cli", "rxjs", "sequelize.js", "react-hooks", "discord.js",
           "react.js", "svelve-3", "konvajs", "npm-install", "angular-material", "requirejs", "pdfjs", "npm",
           "nuxt.js", "svelve", "vuejs-datepicker", "angular6", "scala.js", "vue-components", "jquery-ui",
           "momentjs", "vue-component"]
DOTNET_TAGS = ["winforms", ".net-core", "entity-framework-core", "wpf", "uwp", "signalr", "visual-studio-code",
               "entity-framework", "linq", "autofac", "entity-framework-6", "blazor", "wcf", "visual-studio-2010",
               "razor-pages", "visual-studio-2017", "ef-core-3.1", ".net-core-3.1", "entity-framework-5"]
ANDROID_TAGS = ["android-studio", "retrofit", "android", "android-intent","android-service", "android-recyclerview",
                "android-layout", "android-webview", "genymotion", "android-databinding", "androidx",
                "android-camera2", "android-fragments", "android-security", "android-studio-3.6", "android-room"]
DJANGO_TAGS = ["django", "django-templates", "django-models", "django-apps", "django-rest-framework",
               "django-channels", "django-migrations"]
AMAZON_TAGS = ["amazon-redshift", "aurelia", "amazon-web-services", "amazon-elastic-beanstalk", "amazon-rds",
               "amazon-dynamodb", "amazon-cloudformation", "amazon-echo", "amazon-sagemaker", "amazon-cloudwatch",
               "aws-fargate", "amazon-athena", "aws-java-sdk", "amazon-cloudfront"]
GOOGLE_TAGS = ["google-apps-script", "google-maps", "google-apps-script", "google-maps-markers", "google-cloud-storage",
               "google-sheets", "google-analytics", "google-search-console", "google-earth-engine", "google-drive-api",
               "google-spreadsheet", "youtube-iframe-api", "google-kubernetes-engine", "google-sheets-formula",
               "google-translate", "youtube", "google-colaboratory", "recaptcha", "google-chrome", "google-classroom",
               "google-sheets-importxml", "google-cloud-dataflow", "google-assistant-sdk", "gmail-api",
               "google-contacts-api", "google-content-api", "google-data-studio", "youtube-data-api",
               "firebase-storage", "google-apis-explorer", "google-people", "firebase-app-distribution", "google-oauth",
               "google-calendar-api", "google-cloud-automl", "google-docs-api", "google-admin-sdk", "google-play"]
HADOOP_TAGS = ["oozie", "hive", "cloudera", "hapood2"]
GCP_TAGS = ["google-cloud-platform", "google-bigquery", "google-text-to-speech", "google-cloud-firestore",
            "google-compute-engine"]
PY_LIB_TAGS = ["pyautogui", "airflow"]


STOP_TAGS = ["cuda", "ionic2", "ionic-framework", "cordova", "mysql", "forms", "unity3d", "bixby",
             "google-app-engine", "kendo-grid", "angularfire2", "firebase", "electron", "facebook", "pascal",
             "office365", "salesforce", "crm", "alexa-skill", "adobe", "doxygen", "sybase", "oracle12c",
             "lodash", "swing", "javafx", "groovy", "neo4j", "pygame", "scene2d", "grails", "asterisk",
             "tkinter", "wildfly-9", "alexa-skills-kit", "google-cloud-function", "xslt-2.0", "foursquare",
             "twilio", "tfs", "tfs2017", "jquery", "struts2", "kendo-ui", "sharepoint", "vbscript", "windows",
             "dynamics-crm", "vulkan", "visual-studio-2012", "odata", "brainfuck", "druid", "mod-rewrite", ".htaccess",
             "sap", "highcharts", "vba", "sharepoint-2010", "vb.net",  "excel", "devexpress", "newrelic",
             "datagridview", "crystal-reports", "charts.js", "carousel", "jmeter", "fortran", "paypal-webhooks",
             "firebase-cloud-messaging", "word", "qt5", "pyqt", "silverstripe", "autolisp", "clickonce", "octobercms",
             "cloudkit", "facebook-graph-api",  "regex", "ionic3", "photoshop", "microk8s", "stata",
             "openwrt", "identityserver3", "wildfly", "nhibernate", "apache-cayenne", "opencv", "alexa",
             "playframework", "codenvy", "botframework", "mobx", "eclipse", "transpose", "phantomjs", "ruby-on-rails",
             "flask", "ibm-mq", "discord.py-rewrite", "ibm-watson", "clisp", "dafny", "xsd", "dynamics-ax-2012",
             "xpath", "facebook-instant-articles", "visio", "apollo-server", "orchardcms", "opencmis",
             "docplexcloud",  "actionscript-3", "gis", "openlayers", "devextreme", "sendgrid", "libreoffice-calc",
             "js-pdf", "anylogic", "cpanel", "zend-studio", "phonegap", "gluon", "figma", "amibroker", "playwright",
             "google-maps-api-3", "parse.com", "react-native", "woocommerce", "amazon-s3", "jhipster", "chart.js",
             "openerp", "visual-c++", "wordpress-gutenberg", "bitcoin", "passport.js", "haproxy",
             "primeng", "nativescript", "ckeditor4.x", "pentaho", "postman", "mondrian", "instagram", "jspdf",
             "socialshare", "markojs", "jrecorder", "jenkins-pipeline", "modelica", "office-addins", "elisp",
             "slack", "automapper-5", "unity2d", "polly", "excel-interop", "unity5", "sharppcap",
             "tibco-ems", "sonarqube", "netlogo", "webrtc", "gml", "excel-formula", "ada", "ada95",
             "heroku", "sails.js", "waterline", "certbot", "snapchat", "feathersjs", "orientdb", "ogg", "ibm-mq",
             "pdfkit", "oracle-data-integrator", "rstudio", "blender", "coq", "slim4", "mqtt", "mailgun", "openam",
             "ffmpeg", "dreamfactory", "ms-access", "wso2esb", "ms-access-2013", "cygwin", "adobe-indesign",
             "picturefill", "lotus-notes", "ionic4", "google-finance", "react-native-android", "3dsmax",
             "microsoft-edge", "apache-camel", "cplex", "apache-nifi", "evernote", "inno-setup", "dialogflow",
             "ruby-on-rails-4", "slider", "plotly", "owl-carousel", "vis.js", "tizen", "geoserver", "mapbox", "froala",
             "navision", "bots", "telegram-bot", "office-js", "kong", "guile", "chromecast", "xsl-fo",
             "dropbox-api", "mono", "hangfire", "vsix", "exchange-server", "sharepoint-2013", "flux", "webforms",
             "imagemagick", "google-sheets-api", "react-native-ios", "active-directory", "acumatica",
             "flash", "dailymotion-api", "openstreetmap", "rhino", "google-trends", "angular-dart", "angular2-dart",
             "payara", "polymer", "cloudfoundry", "svn", "amtlr", "fancybox", "maxima", "autohotkey",
             "office-scripts", "zoom", "raspberry-pi", "coldfusion", "oracle-sqldeveloper", "jekyll", "antlr",
             "c3.js", "selenium", "onedrive-api", "visual-foxpro", "outlook", "selenium-webdriver", "mirth", "video.js",
             "imagemagick-convert", "aforge", "square-connect", "arduino", "alloy-ui", "mojolicious",
             "mithril.js", "opentok", "office365api", "gremlin", "cypress", "couchdb", "flash-admin", "guzzle6",
             "iframe", "pouchdb", "leaflet", "soundcloud", "jtable", "citrix", "excel-2010", "cobol",
             "netbeans", "kotlin", "affdex-sdk", "bazel", "adobe-reader", "solr4", "ionic5", "lotus-domino",
             "mono.cecil", "powerpoint", "exchangewebservices", "amcharts", "meteor", "jasper-reports", "sqlalchemy",
             "solaris", "telepot", "excel-vba", "vlc", "informatica", "gimp", "splunk", "influxdb",
             "ghprb", "bitbucket", "openshift", "activemq", "solr", "voicemail", "pug", "itext7",
             "ejs", "grpc", "intel-xdk", "aws-lambda", "okta", "loopbackjs", "flowtype", "visualforce", "jsfeat",
             "tampermonkey", "mariadb", "powershell-3.0", "powershell-4.0", "xamarin.forms", "gitlab",
             "tweenmax", "nunjucks", "blueimp", "google-recaptcha", "discord", "google-visualization", "sweetalert",
             "bacon.js", "thymeleaf", "zebble", "gatt", "docusign", "signalr-hub", "aleagpu", "google-api",
             "paypal-ipn", "pdfsharp", "qweb", "karate", "liferay", "elm", "ruby-on-rails-6",
             "dojo", "ms-word", "tampermonkey", "jira", "sapui5", "jszip", "google-form", "jqgrid", "deployd",
             "sinatra", "mediaelement.js", "jwplayer", "netbeans-8", "sidekiq", "powershell-5.0", "xampp", "cgal",
             "chef", "jsonlite", "here-api", "microsoft-graph", "ambari", "hapi", "sentry",
             "ckeditor", "accordion", "masonry", "shopify", "google-drive-sdk", "whatsapp", "slick.js", "tinymce",
             "skulpt", "ormlite-servicestack", "apex", "keycloak", "concourse", "oracle-apex", "artifactory",
             "postgis", "pgadmin-4", "pgadmin", "eclipselink", "ibm-bluemix", "битрикс", "jwt", "expo",
             "flutter", "skype", "kiwi-tcms", "angular", "uipath-studio", "flutter-desktop", "autodesk-forge",
             "rust", "scala", "oracle", "powershell", "xamarin", "c#", ".net", "svg", "behat", "nsis", "installer",
             "twitter-bootstrap", "gulp", "google-chrome-extension", "latex", "soap", "puppeteer", "xero-api",
             "typescript",  "r", "haskell", "asp.net-core", "erlang", "elixir", "ejabber", "modbus",
             "rubygems", "matlab", "wxwidgets", "verilog", "asp.net-web-api", "xamarin", "asp.net-mvc",
             "visual-studio-2019", "objective-c", "perforce", "microsoft-graph-teams", "puppet", "mediawiki",
             "sap-cloud-sdk", "svelte", "jsf", "xamarin.ios", "matlab-figure", "mainframe", "traefic",
             "unreal-engine4", "lua", "asp.net", "cisco", "react-redux", "ocaml", "pine-script", "filezilla",
             "ruby", "octave", "vb6", "orocrm", "zurb-foundation", "fortran90", "microsoft-teams", "clarion",
             "asp-classic", "moodle", "perl", "scheme" "discord.js", "robotframework", "kivy", "odoo",
             "ibm-cloud", "lisp", "fuchsia", "vuetify.js", "visual-studio", "qt", "minecraft", "crystal-lang",
             "asciidoc", "mailchimp", "access", "nopcommerce", "godot", "openapi", "zapier", "presto",
             "linkedin", "racket", "flutter-web", "openmdao", "ballerina", "jitsi-meet", "hasura", "corda", "sms",
             "delphi", "django-forms", "zabbix", "shiny", "ethereum", "mips", "assembly", "asp.net-identity", "seq2seq",
             "teradata", "vidyo", "stripe-payments", "freeradius", "akka", "vala", "apollo", "cloudinary",
             "dart", "twilio-studio", "robot.txt", "youtube-api", "next.js", "pyqt5", "julia", "asp",
             "twilio-programmable-chat", "bibtex", "admob", "aerospike", "antd", "epplus-4", "windows-10",
             "remote-desktop", "sagemath", "clonezilla", "traefik", "windows-store-apps", "openoffice.org",
             "gradle", "haxe", "xamarin.android", "vhdl", "vue-tables-2", "apache-spark", "pyspark", "ghost-blog",
             "couchbase", "opengl", "angular7", "symphony4", "access-vba", "terraform", "aframe", "mfc",
             "sharepoint-online", "clojurescript", "cucumber", "vmware", "apache-flink", "scrapy",
             "pymongo", "mlflow", "beautifulsoup", "gekko", "oracle11g", "xslt", "tortoisesvn", "draftjs",
             "xmpp", "odoo1-12", "ldap", "jenkins", "gatsby", "iis", "raku", "paypal", "wso2", "hadoop",
             "notepad++", "dtd", "websphere", "oracle-xe", "common-lisp", "bison", "qgis", "kusto",
             "seo", "maximo", "spacy", "nestjs", "tableau", "prolog", "drake", "hololens", "heatmap",
             "vtk", "amazon-ec2", "boto3", "sublimetext", "vaadin", "emacs", "opencart", "pdftk",
             "activemq-artemis", "artemis", "appium", "carrierwave", "dplyr", "vert.x", "activitypub",
             "prestashop", "windows-defender", "r-markdown", "asciidoctor", "azerothcore",
             "sublimetext3", "roblox", "luis", "marklogic", "word-addins", "eclipse-rcp", "jitter"]

STOP_TAGS = STOP_TAGS + PHP_TAGS + JS_TAGS + DOTNET_TAGS + ANDROID_TAGS + DJANGO_TAGS + AMAZON_TAGS + GOOGLE_TAGS + \
            HADOOP_TAGS + GCP_TAGS + PY_LIB_TAGS

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
             "spring-boot-activator", "spring-data-redis"]
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

    def first_level_classification(self, tags: List[str]) -> Optional[str]:
        for rule in self.first_level_rules:
            if rule["include"] == "*":
                return rule["result"]
            else:
                for rule_tag in rule["include"].split(","):
                    if rule_tag in tags:
                        return rule["result"]

        return "none"

    def second_level_classification(self, tags: List[str], first: str) -> Optional[str]:
        for rule in SECOND_LEVEL_RULES:
            if rule["first"] == first and rule["include"] in tags:
                return rule["result"]

        return "none"

    def classify(self, questions):
        result = []
        for q in questions:
            if not self.has_stop_tag(q["tags"]):
                q["first"] = self.first_level_classification(q["tags"])
                q["second"] = self.second_level_classification(q["tags"], q["first"])
                result.append(q)
        return result
