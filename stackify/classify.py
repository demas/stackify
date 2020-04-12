from typing import List, Optional

STOP_TAGS = ["php", "django", "cuda", "ionic2", "ionic-framework", "cordova", "wordpress", "laravel", "winforms", "mysql", "forms", "unity3d",
	"google-app-engine", "kendo-grid", "angularfire2", "firebase", "electron", "facebook", "pascal", "office365", "salesforce", "crm",
	"knockout.js", "lodash", "extjs", "swing", "javafx", "groovy", "neo4j", "google-cloud-storage", "pygame", "scene2d", "tkinter", "wildfly-9",
	"twilio", "tfs", "tfs2017", "jquery", "struts2", "kendo-ui", "vue.js", "vuejs2", "sharepoint", "vbscript", "dynamics-crm",
	"sap", "highcharts", "three.js", "d3.js", "ember.js", "vba", "sharepoint-2010", "vb.net", "amazon-web-services", "excel", "devexpress",
	"datagridview", "crystal-reports", "google-apps-script", "charts.js", "signalr", "carousel", "firebase-cloud-messaging", "word",
	"cloudkit", "facebook-graph-api", "amazon-web-services", "gruntjs", "regex", "handlebars.js", "google-apps-script",
	"laravel-5.1", "openwrt", "identityserver3", "wildfly", "nhibernate", "apache-cayenne", "opencv", "alexa",
	"playframework", "codenvy", "botframework", "mobx", "eclipse", "transpose", "phantomjs", "ruby-on-rails", "flask", "ibm-mq",
	"docplexcloud", "underscore.js", "youtube-iframe-api", "actionscript-3", "gis", "openlayers", "devextreme", "google-maps", "js-pdf",
	"google-maps-api-3", "parse.com", "react-native", "woocommerce", "amazon-s3", "jhipster", "chart.js", "openerp",
	"primeng", "nativescript", "ckeditor4.x", "pentaho", "postman", "mondrian", "instagram", "jspdf", "socialshare", "markojs", "jrecorder",
	"slack", "google-analytics", "automapper-5", "unity2d", "polly", "excel-interop", "unity5", "sharppcap", "tibco-ems", "sonarqube",
	"heroku", "sails.js", "waterline", "certbot", "snapchat", "feathersjs", "orientdb", "ogg", "ibm-mq", "pdfkit",
	"ffmpeg", "dreamfactory", "ms-access", "wso2esb", "ms-access-2013", "cakephp", "cygwin", "amazon-redshift", "aurelia", "picturefill",
	"ruby-on-rails-4", "slider", "plotly", "owl-carousel", "vis.js", "tizen", "geoserver", "mapbox", "froala", "navision",
	"dropbox-api", "mono", "hangfire", "vsix", "exchange-server", "sharepoint-2013", "flux", "webforms", "imagemagick", "google-sheets-api",
	"flash", "dailymotion-api", "openstreetmap", "rhino", "google-trends", "angular-dart", "angular2-dart", "payara", "polymer", "cloudfoundry",
	"c3.js", "joomla", "selenium", "onedrive-api", "visual-foxpro", "outlook", "selenium-webdriver", "mirth", "video.js",
	"imagemagick-convert", "laravel-5", "aforge", "square-connect", "arduino", "alloy-ui", "mojolicious", "mithril.js", "opentok",
	"google-spreadsheet", "iframe", "google-maps-markers", "pouchdb", "leaflet", "soundcloud", "jtable", "netbeans", "kotlin", "affdex-sdk",
	"mono.cecil", "powerpoint", "exchangewebservices", "amcharts", "meteor", "jasper-reports", "sqlalchemy", "solaris",
	"ghprb", "bitbucket", "google-search-console", "openshift", "activemq", "solr", "voicemail", "pug",
	"ejs", "grpc", "intel-xdk", "aws-lambda", "okta", "loopbackjs", "flowtype", "visualforce", "jsfeat", "tampermonkey",
	"symfony", "tweenmax", "backbone.js", "nunjucks", "blueimp", "google-recaptcha", "discord", "google-visualization", "sweetalert",
	"bacon.js", "thymeleaf", "zebble", "gatt", "docusign", "signalr-hub", "aleagpu", "google-api", "paypal-ipn", "pdfsharp", "yii2", "qweb",
	"dojo", "ms-word", "tampermonkey", "jira", "sapui5", "jszip", "google-form", "jqgrid", "deployd", "sinatra", "mediaelement.js", "jwplayer",
	"ckeditor", "accordion", "masonry", "shopify", "google-drive-sdk", "whatsapp", "slick.js", "tinymce", "skulpt", "ormlite-servicestack",
	"postgis", "pgadmin-4", "pgadmin", "eclipselink", "oozie", "ibm-bluemix", "битрикс", "jwt", "expo",
	"android-studio", "flutter", "google-sheets", "reactjs", "node.js", "skype", "kiwi-tcms", "angular",
	"angular3", "angular4", "angular5", "rust", "scala", "oracle", "powershell", "xamarin", "c#", ".net", "svg",
	"twitter-bootstrap", "gulp", "android", "mocha", "chai", "webpack", "eslint", "redux", "google-chrome-extension",
	"typescript", "javascript", "r", "haskell", "kubernetes", "asp.net-core", "php-curl", "erlang", "elixir",
	"rubygems", "matlab", "wxwidgets", "verilog", "asp.net-web-api", "xamarin", "asp.net-mvc", "visual-studio-2019",
	"wpf", "unreal-engine4", "lua", "drupal-8", "asp.net", "cisco", "react-redux", "ocaml", "pine-script", "ruby",
	"asp-classic", "moodle", "entity-framework", "perl", "scheme" "discord.js", "robotframework", "kivy", "odoo",
	"ibm-cloud", "svelve", "angularjs", "lisp", "fuchsia", "vuetify.js", "visual-studio", "qt", "minecraft", "linkedin",
	"delphi", "django-forms", "zabbix", "shiny", "ethereum", "mips", "assembly", "asp.net-identity", "seq2seq",
	"entity-framework-core", "teradata", "typo3-8.x", "vidyo", "stripe-payments", "freeradius", "akka", ".net-core",
	"dart", "twilio-studio", "visual-studio-code", "robot.txt", "youtube-api", "uwp", "next.js", "pyqt5", "julia",
	"gradle", "haxe", "xamarin.android", "vhdl", "vue-tables-2", "typo3", "laravel-6", "apache-spark", "pyspark",
	"couchbase", "django-templates", "retrofit", "opengl", "angular7", "symphony4", "access-vba", "terraform",
	"sharepoint-online", "google-drive-api", "clojurescript", "cucumber", "vmware","apache-flink", "scrapy",
	"pymongo", "mlflow", "beautifulsoup"]

HIDE_TAGS = ["none", "ios", "machine-learning", "azure", "mongodb", "sql-server", "web", "java", "fsharp",
					 "clojure", "business-intelligence", "kafka", "ansible"]

MACHINE_LEARNING_TAGS = ["machine-learning","anaconda","tensorflow","nltk","pandas","classification","keras",
						 "numpy","pytorch","classification","adaboost","matplotlib","scikit-learn","deep-learning",
						 "reinforcement-learning"]
AZURE_TAGS = ["azure","azure-functions","azure-data-studio","azureservicebus","azure-devops","azure-web-sites",
			  "azure-storage"]
JAVA_TAGS = ["spring","spring-boot","java","java-8","tomcat"]
ARCHITECTURE_TAGS = ["oop","software-design","architecture"]
C_TAGS = ["c","c++","gcc","c++11","c++14"]
IOS_TAGS = ["swift","xcode","swiftui","ios","swift3","swift4"]

FIRST_LEVEL_RULES = [
	{"site": "stackoverflow", "include": "intellij-idea", "result": "intellij" },
	{"site": "stackoverflow", "include": "vim", "result": "vim" },
	{"site": "stackoverflow", "include": "ansible", "result": "ansible" },
	{"site": "stackoverflow", "include": "redis", "result": "redis" },
	{"site": "stackoverflow", "include": "prometheus", "result": "prometheus" },
	{"site": "stackoverflow", "include": "elasticsearch", "result": "elasticsearch" },
	{"site": "stackoverflow", "include": "cassandra", "result": "cassandra" },
	{"site": "stackoverflow", "include": "apache-kafka", "result": "kafka" },
	{"site": "stackoverflow", "include": "rabbitmq", "result": "rabbitmq" },
	{"site": "stackoverflow", "include": "unit-testing", "result": "unit testing"},
	{"site": "stackoverflow", "include": ",".join(ARCHITECTURE_TAGS), "result": "architecture" },
	{"site": "stackoverflow", "include": ",".join(MACHINE_LEARNING_TAGS), "result": "machine-learning"},
	{"site": "stackoverflow", "include": ",".join(AZURE_TAGS), "result": "azure" },
	{"site": "stackoverflow", "include": "f#", "result": "fsharp" },
	{"site": "stackoverflow", "include": "clojure", "result": "clojure" },
	{"site": "stackoverflow", "include": "git", "result": "git" },
	{"site": "stackoverflow", "include": "github", "result": "git" },
	{"site": "stackoverflow", "include": "docker", "result": "docker" },
	{"site": "stackoverflow", "include": "sql-server", "result": "sql-server" },
	{"site": "stackoverflow", "include": "bash", "result": "bash" },
	{"site": "stackoverflow", "include": "sed", "result": "bash" },
	{"site": "stackoverflow", "include": "awk", "result": "bash" },
	{"site": "stackoverflow", "include": ",".join(JAVA_TAGS), "result": "java" },
	{"site": "stackoverflow", "include": ",".join(IOS_TAGS), "result": "ios"},
	{"site": "stackoverflow", "include": "go", "result": "go" },
	{"site": "stackoverflow", "include": ",".join(C_TAGS), "result": "c" },
	{"site": "stackoverflow", "include": "powerbi", "result": "business-intelligence" },
	{"site": "stackoverflow", "include": "python", "result": "python"},
	{"site": "stackoverflow", "include": "python-3.x", "result": "python"},
	{"site": "stackoverflow", "include": "python-3.8", "result": "python"},
	{"site": "stackoverflow", "include": "python-2.7", "result": "python"},
	{"site": "stackoverflow", "include": "postgresql", "result": "postgresql"},
	{"site": "stackoverflow", "include": "mongodb", "result": "mongodb"},
	{"site": "stackoverflow", "include": "linux", "result": "linux"},
	{"site": "stackoverflow", "include": "html", "result": "web"},
	{"site": "stackoverflow", "include": "css", "result": "web"},
	{"site": "stackoverflow", "include": "networking", "result": "networking"},
	{"site": "stackoverflow", "include": "ssh", "result": "networking"},
	{"site": "stackoverflow", "include": "algorithm", "result": "algorithm"},
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
