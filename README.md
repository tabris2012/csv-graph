# csv-graph
![](https://github.com/tabris2012/csv-graph/workflows/Unit%20Test/badge.svg?branch=dev)

## Remote development in VSCode attaching to dev-container
* Install `Remote - Containers` Extension in VSCode
* In Command Pallet: `Remote-Containers: Open Folder in Container...`, then select the project directory
* Stop containers
  * `$ ./docker.sh down`
* Development container can be opened without VSCode
  * `$ ./docker.sh up`
* Scripts can be executed in container
  * `$ ./docker.sh python -m <path.to.class>`
* Test scripts can be executed in container
  * `$ ./docker.sh test`
  * `$ ./docker.sh python -m unittest <path.to.test.class>`
