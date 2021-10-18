import yaml


def get_yaml(yaml_file_path):
    case_names = []
    requests = []
    expected_results = []

    with open(yaml_file_path, encoding='utf-8') as f:
        data = yaml.safe_load(f)
    test_cases = data['test_cases']
    for case in test_cases:
        case_names.append(case.get('case_name', ''))
        requests.append(case.get('requests', {}))
        expected_results.append(case.get('expected_results', {}))
    parameters = zip(case_names, requests, expected_results)
    return case_names, parameters

