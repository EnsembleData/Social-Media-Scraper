# EnsembleData Python API

[![pypi](https://img.shields.io/pypi/v/ensembledata?color=%2334D058&label=pypi%20package)](https://pypi.org/project/ensembledata/)
![](https://img.shields.io/pypi/pyversions/ensembledata.svg?color=%2334D058alt=%22Supported%20Python%20versions)

## Documentation

Check out the [API docs](https://ensembledata.com/apis/docs) to see which endpoints are available for each social media and for detailed descriptions of their parameters and functionality.

## Installation

Install the package with pip as you would any other python package.

```bash
pip install ensembledata
```

### Requirements

- The package only supports Python 3.7 and above.

## Usage

[Register](https://dashboard.ensembledata.com/register) to get your free API token.

```python
from ensembledata.api import EDClient


client = EDClient("API-TOKEN")
result = client.tiktok.user_info_from_username("daviddobrik")

print("Data: ", result.data)
print("Units charged:", result.units_charged)

# Other Examples:
# result = client.instagram.user_info(username="daviddobrik")
# result = client.youtube.channel_subscribers(channel_id="UCnQghMm3Z164JFhScQYFTBw")
```

#### TikTok Guide
Get started with the [TikTok API Guide](https://github.com/ensembledata/tiktok-scraper). Find out which endpoints are available, and how you can use them with examples using the ensembledata python package.

#### Instagram Guide
Get started with the [Instagram API Guide](https://github.com/ensembledata/instagram-scraper). Find out which endpoints are available, and how you can use them with examples using the ensembledata python package.


&nbsp;

### Missing Endpoints / Parameters

If you find that one of the endpoints from our [API docs](https://ensembledata.com/apis/docs) is not yet available in this package, you can use the `EDClient.request` method to specify the endpoint manually in the meantime. 

```python
from ensembledata.api import EDClient

client = EDClient("API-TOKEN")
result = client.request("/instagram/[example]", params={"foo": "...", "bar": "..."})
```

If you find that one the parameters to an existing endpoint is missing, you can still send this parameter via the `extra_params` dictionary which is available on all endpoint methods. See the example below:
```python
from ensembledata.api import EDClient

client = EDClient("API-TOKEN")
result = client.instagram.user_info(username="...", extra_params={"baz": "..."})
```

&nbsp;

### Handling Errors

In the [API docs](https://ensembledata.com/apis/docs), each endpoint lists a handful of possible errors the API may respond with. You can handle these errors by catching the `EDError` exception. 

```python
from ensembledata.api import EDClient, EDError


client = EDClient("API-TOKEN")
try:
    result = client.tiktok.user_info_from_username("daviddobrik")
except EDError as e:

    # Rate limit exceeded...
    if e.status_code == 429:
        print(e.detail)

    # Subscription expired...
    if e.status_code == 493:
        print(e.detail)

except Exception as e:
    # Some other error occurred, unrelated to the EnsembleData API
    # E.g. httpx.RequestError, json.JSONDecodeError
    pass

    
```

&nbsp;


### Async 

This package provides an asynchronous client, `EDAsyncClient`, which will give you access to async versions of all the same methods that can be found on the `EDClient`. 

```python
import asyncio

from ensembledata.api import EDAsyncClient


async def main():
    client = EDAsyncClient("API-TOKEN")
    result = await client.tiktok.user_info_from_username("daviddobrik")

if __name__ == "__main__":
    asyncio.run(main())
```

### Types

The package uses type hints, and is type checked with the latest version of `mypy`. If you experience any type checking related issues with the package, please let us know by creating an issue.
