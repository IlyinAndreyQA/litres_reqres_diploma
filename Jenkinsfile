pipeline {
    agent any

    environment {
        PYTHON = '/Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11'
    }

    parameters {
        choice(name: 'TEST_SCOPE', choices: ['web_api', 'web', 'api', 'mobile'], description: 'Test suite to run')
        string(name: 'WEB_BASE_URL', defaultValue: 'https://www.litres.ru', description: 'Litres base URL')
        string(name: 'API_BASE_URL', defaultValue: 'https://reqres.in/api', description: 'Reqres base URL')
        password(name: 'REQRES_API_KEY', defaultValue: '', description: 'Reqres API key')
        booleanParam(name: 'RUN_MOBILE', defaultValue: false, description: 'Run Appium mobile tests')
        string(name: 'BROWSER_NAME', defaultValue: 'chrome', description: 'Browser name')
        string(name: 'BROWSER_VERSION', defaultValue: '128.0', description: 'Browser version')
        string(name: 'REMOTE_URL', defaultValue: '', description: 'Selenoid or Selenium Grid URL')
        choice(name: 'MOBILE_CONTEXT', choices: ['local', 'browserstack'], description: 'Mobile run context')
    }

    stages {
        stage('Install dependencies') {
            steps {
                sh '${PYTHON} -m venv .venv'
                sh '.venv/bin/python -m pip install --upgrade pip'
                sh '.venv/bin/python -m pip install -r requirements.txt'
            }
        }

        stage('Run WEB and API tests') {
            when {
                expression { params.TEST_SCOPE == 'web_api' }
            }
            steps {
                sh '.venv/bin/python -m pytest tests/web tests/api --browser_name=${BROWSER_NAME} --browser_version=${BROWSER_VERSION} --alluredir=allure-results'
            }
        }

        stage('Run WEB tests') {
            when {
                expression { params.TEST_SCOPE == 'web' }
            }
            steps {
                sh '.venv/bin/python -m pytest tests/web --browser_name=${BROWSER_NAME} --browser_version=${BROWSER_VERSION} --alluredir=allure-results'
            }
        }

        stage('Run API tests') {
            when {
                expression { params.TEST_SCOPE == 'api' }
            }
            steps {
                sh '.venv/bin/python -m pytest tests/api --alluredir=allure-results'
            }
        }

        stage('Run MOBILE tests') {
            when {
                expression { params.TEST_SCOPE == 'mobile' }
            }
            steps {
                sh 'if [ "${RUN_MOBILE}" = "true" ]; then .venv/bin/python -m pytest tests/mobile --mobile_context=${MOBILE_CONTEXT} --alluredir=allure-results; else echo "Mobile tests skipped: RUN_MOBILE=false"; fi'
            }
        }
    }

    post {
        always {
            allure commandline: 'Allure', includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
    }
}
