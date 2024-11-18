pipeline {
    agent {
        docker {
            image 'python:3.9-alpine' // Use the appropriate Python version with Alpine
            args '-u' // Run as unprivileged user
        }
    }

    options {
        // Reuse the same node for all stages
        reuseNode true
    }

    environment {
        // Set the Django settings module to your app's settings
        DJANGO_SETTINGS_MODULE = 'todo_list.settings'
        VENV_DIR = 'venv'
        PORT = '8000' // Port to run the Django app
    }

    stages {
        stage('Setup Environment') {
            steps {
                // Install dependencies and create a virtual environment
                sh '''
                apk add --no-cache gcc musl-dev libffi-dev python3-dev
                python3 -m venv ${VENV_DIR}
                . ${VENV_DIR}/bin/activate && pip install --upgrade pip
                . ${VENV_DIR}/bin/activate && pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                // Run your Django tests
                sh '. ${VENV_DIR}/bin/activate && python manage.py test'
            }
        }

        stage('Build') {
            steps {
                // You can add build steps here if needed
                echo 'Building the Django app...'
            }
        }

        stage('Run Application') {
            steps {
                // Run the Django application
                sh '''
                . ${VENV_DIR}/bin/activate
                python manage.py migrate
                python manage.py collectstatic --noinput
                python manage.py runserver 0.0.0.0:${PORT} &
                '''
                // Note: The '&' runs the server in the background
            }
        }
    }

    post {
        success {
            echo 'Deployment successful! The Django app is running.'
        }
        failure {
            echo 'Deployment failed!'
        }
    }
}
