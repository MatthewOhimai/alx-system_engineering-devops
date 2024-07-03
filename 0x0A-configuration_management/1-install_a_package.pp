# Ensure python3.8 is installed with the specified version
package { 'python3.8':
	ensure => '3.8.10',
	provider => 'pip3',
}

# Ensure Flask is installed with the specified version
package { 'Flask':
	ensure => '2.1.0',
	provider => 'pip3',
}

# Ensure Werkzeug is installed with the specified version
package { 'Werkzeug':
	ensure => '2.1.1',
	provider => 'pip3',
	require => Package['Flask'],
}
