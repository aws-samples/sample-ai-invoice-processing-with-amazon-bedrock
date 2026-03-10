# Contributing Guidelines

Thank you for your interest in contributing to InvoiceFlow AI. Whether it's a bug report, new feature, correction, or additional
documentation, we greatly value feedback and contributions from our community.

Please read through this document before submitting any issues or pull requests to ensure we have all the necessary
information to effectively respond to your bug report or contribution.


## Reporting Bugs/Feature Requests

We welcome you to use the GitHub issue tracker to report bugs or suggest features.

When filing an issue, please check existing open, or recently closed, issues to make sure somebody else hasn't already
reported the issue. Please try to include as much information as you can. Details like these are incredibly useful:

* A reproducible test case or series of steps
* The version of our code being used
* Any modifications you've made relevant to the bug
* Anything unusual about your environment or deployment
* AWS region and services being used
* Sample invoice or contract files (with sensitive data removed)


## Contributing via Pull Requests
Contributions via pull requests are much appreciated. Before sending us a pull request, please ensure that:

1. You are working against the latest source on the *main* branch.
2. You check existing open, and recently merged, pull requests to make sure someone else hasn't addressed the problem already.
3. You open an issue to discuss any significant work - we would hate for your time to be wasted.

To send us a pull request, please:

1. Fork the repository and follow the [deployment guide](code/invoiceFlow-AI/DEPLOYMENT_GUIDE.md) for setting up InvoiceFlow AI.

```sh
git clone https://github.com/{your-account}/invoiceflow-ai.git
```

2. Then, prepare your local environment before you move forward with the development.

```sh
cd invoiceflow-ai
git checkout -b <<BRANCH-NAME>>
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

3. Modify the source; please focus on the specific change you are contributing. If you also reformat all the code, it will be hard for us to focus on your change.

4. Ensure deployment/testing to personal AWS environments pass.

- Set up your AWS credentials and region
- Deploy the infrastructure using the deployment script:

```sh
cd code/invoiceFlow-AI/backend/infrastructure
./create_deployment_role.sh
export DEPLOYMENT_ROLE_ARN='arn:aws:iam::ACCOUNT_ID:role/InvoiceFlowDeploymentRole'
python cognito_deployment.py
```

- Test the application:

```sh
cd ../
streamlit run simplified_app.py
```

5. Commit to your fork using clear commit messages following [Conventional Commits](https://www.conventionalcommits.org/).
6. Send us a pull request, answering any default questions in the pull request interface.
7. Pay attention to any automated CI failures reported in the pull request, and stay involved in the conversation.

GitHub provides additional document on [forking a repository](https://help.github.com/articles/fork-a-repo/) and
[creating a pull request](https://help.github.com/articles/creating-a-pull-request/).


## Development Guidelines

### Code Standards
- Follow PEP 8 for Python code formatting
- Add docstrings for all functions and classes
- Include type hints where appropriate
- Write unit tests for new functionality
- Update documentation for any changes

### Testing
- Test with sample invoice and contract files
- Verify AWS Bedrock integration works correctly
- Ensure Knowledge Base search returns relevant results
- Test all approval recommendation scenarios

### Documentation
- Update README.md for any new features
- Add examples for new functionality
- Update deployment guide if infrastructure changes
- Include screenshots for UI changes


## Finding contributions to work on
Looking at the existing issues is a great way to find something to contribute on. As our projects, by default, use the default GitHub issue labels (enhancement/bug/duplicate/help wanted/invalid/question/wontfix), looking at any 'help wanted' issues is a great place to start.

### Areas for Contribution
- **Invoice Processing**: Improve extraction accuracy or add support for new invoice formats
- **Contract Validation**: Enhance validation rules or add new compliance checks
- **User Interface**: Improve the Streamlit interface or add new visualization features
- **Documentation**: Improve setup guides, add tutorials, or create video walkthroughs
- **Testing**: Add test cases, improve test coverage, or create integration tests
- **Performance**: Optimize processing speed or reduce AWS costs


## Code of Conduct
This project has adopted the [Amazon Open Source Code of Conduct](https://aws.github.io/code-of-conduct).
For more information see the [Code of Conduct FAQ](https://aws.github.io/code-of-conduct-faq) or contact
opensource-codeofconduct@amazon.com with any additional questions or comments.


## Security issue notifications
If you discover a potential security issue in this project we ask that you notify AWS/Amazon Security via our [vulnerability reporting page](http://aws.amazon.com/security/vulnerability-reporting/). Please do **not** create a public github issue.


## Licensing

See the [LICENSE](LICENSE) file for our project's licensing. We will ask you to confirm the licensing of your contribution.