# Configure and use multiple GitHub accounts in GitHub Desktop. 
## Here's how you can do it:

### Using GitHub Desktop

1. **Add your first account:**
   - Open GitHub Desktop.
   - Go to `File` > `Options` (on Windows) or `GitHub Desktop` > `Preferences` (on macOS).
   - Click on `Accounts`.
   - Click the `Sign in` button and log in with your first GitHub account.

2. **Add a second account using Git:**
   - While GitHub Desktop itself doesn’t directly support managing multiple accounts, you can switch between accounts by using different repositories tied to different accounts.
   - Open a terminal or command prompt.
   - Configure the second account by setting up a new SSH key and adding it to your second GitHub account.

### Configuring Multiple Accounts in Git

1. **Generate SSH Keys:**
   - Generate a new SSH key pair for your second GitHub account:
     ```bash
     ssh-keygen -t rsa -C "youremail@example.com"
     ```
   - Save the key with a different name, for example, `id_rsa_second_account`.

2. **Add SSH Keys to SSH Agent:**
   - Start the SSH agent:
     ```bash
     eval "$(ssh-agent -s)"
     ```
   - Add both keys to the SSH agent:
     ```bash
     ssh-add ~/.ssh/id_rsa
     ssh-add ~/.ssh/id_rsa_second_account
     ```

3. **Add SSH Keys to GitHub:**
   - Copy the contents of your new public key to your clipboard:
     ```bash
     cat ~/.ssh/id_rsa_second_account.pub
     ```
   - Add this key to your second GitHub account via the GitHub website.

4. **Configure SSH Config File:**
   - Edit the SSH config file:
     ```bash
     nano ~/.ssh/config
     ```
   - Add the following configurations:
     ```plaintext
     Host github.com
       HostName github.com
       User git
       IdentityFile ~/.ssh/id_rsa

     Host github-second
       HostName github.com
       User git
       IdentityFile ~/.ssh/id_rsa_second_account
     ```

5. **Clone Repositories Using Different Accounts:**
   - For repositories associated with your first account, clone them normally:
     ```bash
     git clone git@github.com:username/repo.git
     ```
   - For repositories associated with your second account, use the alias:
     ```bash
     git clone git@github-second:username/repo.git
     ```

### Switching Between Accounts in GitHub Desktop

Since GitHub Desktop does not natively support multiple accounts, you can use the Git command line to manage your repositories with different accounts as described above. GitHub Desktop will recognize the settings you have configured for each repository.

By following these steps, you can effectively manage multiple GitHub accounts on your system and use GitHub Desktop to work with repositories tied to different accounts.