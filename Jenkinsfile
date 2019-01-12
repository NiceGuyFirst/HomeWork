node {
    def app

    stage('Clone repository') {
        /* Let's make sure we have the repository cloned to our workspace */

        checkout scm
    }

    stage('Verify MD5') {
        echo "Checking MD5"
        sh "md5sum -c main.md5"
      
    }

    stage('Execute') {
        sh 'python main.py'
    }

    stage("validate") {       
            sh 'python -m json.tool data.json'
            
    }
    
}