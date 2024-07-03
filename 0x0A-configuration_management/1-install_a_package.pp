#Installation Of Flask Package Using Puppet

package {'Python 3.8':
  version  => '3.8.10',
  provider => 'pip3',
}

package {'Flask':
  version  => '2.1.0',
  provider => 'pip3',
}

package {'Werkzeug':
  version  => '2.1.1'
  provider => 'pip3',
  require  => package['Flask'],
}
