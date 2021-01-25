<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h2 align="center">The Last Hunt (TLH)</h2>
  <h2 align="center">Subscribe</h2>

  <p align="center">
    An awesome way to subscribe to the latest sales on your favorite brands on The Last Hunt!
    <br />
  </p>
</p>
<br />

## About The Project

I wanted to get email notifications about specific brand sales on the website called The Last Hunt which made me build this. Since popular brands get sold out quick, this would in theory boost your chances of getting a good deal by getting an early notification.

### Built With

This was built using Python and the following packages:

-   [requests](https://requests.readthedocs.io/en/master/)
-   [yagmail](https://yagmail.readthedocs.io/en/latest/)
-   [keyring](https://pypi.org/project/keyring/)

<!-- GETTING STARTED -->

## Getting Started

### Installation

-   Clone repo

```sh
git clone https://github.com/mikesmvl/tlh-subscribe.git
```

-   Install packages

```sh
cd tlh-subscribe
pip install -r requirements.txt
```

### Prerequisites

-   If using 2FA, create an app password for your email
    [How to create app password with Google](https://support.google.com/accounts/answer/185833?hl=en)

-   Add email and password to keyring

1. Create

```sh
touch kr.py
vim kr.py
```

2. Write

```python
import yagmail
yagmail.register('email', 'app/password')
```

3. Run and delete

```sh
python kr.py
rm kr.py
```

-   Update sender, recipient and email title in [config.json](https://github.com/MikeSmvl/tlh-subscribe/blob/master/config.json)

```js
// config.json
{
    ...
    "recipient": "your email here",
    "sender": "your email here",
    "emailTitle": "email title here"
}
```

<!-- USAGE EXAMPLES -->

## Usage

### Using Cron Jobs

```sh
crontab -e
# Run every 6 hours
0 */6 * * * path/to/python path/to/tlh-subscribe/subscriber.py
```

<!-- ROADMAP -->

## Roadmap

-   [x] Keep track of seen products
-   [x] Send emails on new products
-   [x] Config file
-   [ ] Specify brand(s) in config
-   [ ] Automatically find query url
-   [ ] Multiple recipients
-   [ ] CLI installation

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.
