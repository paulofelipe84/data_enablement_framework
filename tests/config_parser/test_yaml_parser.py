import pytest
from src.config_parser.yaml_parser import YAMLParser

def test_yaml_parser_success(tmp_path):
    yaml_content = """
    pipeline:
      name: test_pipeline
      contracts:
        - name: test_contract
          schema:
            - table: users
              fields:
                - name: id
                  type: integer
                  constraints: [primary_key]
    """

    yaml_file = f'{tmp_path}/test_config.yaml'
    yaml_file.write_text(yaml_content)

    parser = YAMLParser(filepath=str(yaml_file))
    result = parser.parse()

    assert result['pipeline']['name'] == 'test_pipeline'
    assert result['pipeline']['contracts'][0]['schema'][0]['table'] == 'users'
