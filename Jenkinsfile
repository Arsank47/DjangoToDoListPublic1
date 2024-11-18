pipeline {
    agent {
        docker {
            image 'python:3.9-alpine' // Use the appropriate Python version with Alpine
            args '-u' // Run as unprivileged user
        }
    }

    environment {
        // Set the Django settings module to your app's settings
        DJANGO_SETTINGS_MODULE = 'todo_list.settings'
        VENV_DIR = 'venv'
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

        stage('Deploy') {
            steps {
                // Deploy the application (this is an example using SSH)
                sh '''
                . ${VENV_DIR}/bin/activate
                # Assuming you have a deployment script or command
                scp -r . user@yourserver:/path/to/deploy/
                ssh user@yourserver 'cd /path/to/deploy && source venv/bin/activate && python manage.py migrate && python manage.py collectstatic --noinput && systemctl restart your-django-app.service'
                '''
            }
        }
    }

    post {
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed!'
        }
    }
}
