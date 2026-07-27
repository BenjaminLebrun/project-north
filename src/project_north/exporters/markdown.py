def export_markdown(result):

    profile = result["profile"]
    interpretation = result["interpretation"]

    return f"""# Project North Profile

## Identity

Name: {profile['identity']['name']}

## Expression

Number: {profile['expression']['expression']}

{interpretation['expression']}

## Soul

Number: {profile['soul']['soul']}

{interpretation['soul']}

## Personality

Number: {profile['personality']['personality']}

{interpretation['personality']}

## Life Path

Number: {profile['birth_date']['life_path']['life_path']}

{interpretation['life_path']}
"""