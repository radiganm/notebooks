#!/bin/bash
### ctl
###
### Copyright 2016 Mac Radigan
### All Rights Reserved


  d=${0%/*}; f=${0##*/}; n=${f%.*}; e=${f##*.}
  if [ -f /opt/current.env ]; 
  then
    .  /opt/current.env
  fi

  S__SUCCESS=0
  S__NO_SUCH_COMMAND=1

  usage()
  {
    >&2 cat <<-EOT 
		$f [args]
			  notebook                  - run the notebook
			  notebook-ui               - run the notebook and launch Firefox
EOT
    exit ${S__SUCCESS}
  }

  die()
  {
    code=$1; shift
    msg=$1;  shift
    (>&2 echo "ERROR ${code}: ${msg}")
    exit $code
  }

  warn()
  {
    code=$1; shift
    msg=$1;  shift
    (>&2 echo "WARN ${code}: ${msg}")
    exit $code
  }

  if [[ "$#" == "0" ]]; then
    usage
  fi

  util()
  {
    cmd=$1; shift
    case $cmd in
      find)
        /usr/bin/find $*
        ;;
      shell)
        /bin/bash $*
        ;;
      ls)
        /bin/ls $*
        ;;
      cat)
        /bin/cat $*
        ;;
      ps)
        /bin/ps $*
        ;;
      exec)
        exec $*
        ;;
      *)
        die $S__NO_SUCH_COMMAND "invalid utility: $cmd, must be one of ( find | shell | exec | ls | cat | ps )"
        ;;
    esac
  }

  run()
  {
    #cmd=$1; shift
    #$cmd $*
    ipython notebook --no-browser
  }

  sigint()
  {
    (>&2 echo "shutting down")
    kill 0
  }

  trap sigint SIGINT

  cmd=$1; shift
  case $cmd in
    notebook)
      ipython notebook --ip='*' --no-browser
      ;;
    notebook-ui)
      ipython notebook --ip='*' --browser=firefox
      ;;
    util)
      util $*
      ;;
    *)
      die $S__NO_SUCH_COMMAND "invalid command: $cmd"
      ;;
  esac

  exit $S__SUCCESS

### *EOF*
