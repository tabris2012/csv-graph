FROM python:3.7

RUN apt-get update && apt-get -y install \
    vim

# Install Python libaries
RUN apt-get install -y -q --no-install-recommends \
    python3-dev

## Clean apt-get
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*

## pip install
RUN pip install --upgrade --no-cache-dir pip && \
    pip install pandas matplotlib japanize-matplotlib

RUN wget https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash -O ~/.git-completion.bash && \
    chmod a+x ~/.git-completion.bash && \
    echo "source ~/.git-completion.bash" >> ~/.bashrc

RUN wget https://raw.githubusercontent.com/git/git/master/contrib/completion/git-prompt.sh -O ~/.git-prompt.sh && \
    chmod a+x ~/.git-prompt.sh && \
    echo "source ~/.git-prompt.sh" >> ~/.bashrc && \
    echo 'export PS1='"'"'\[\033[1;32m\]\u\[\033[00m\]:\[\033[1;34m\]\w\[\033[1;31m\]$(__git_ps1)\[\033[00m\] \$ '"'" >> ~/.bashrc
