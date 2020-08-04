# Client configuration file (w/ Puppet)

file_line { 'IdentifyFile':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentifyFile ~/.ssh/holberton',
  match  => '^IdentifyFile',
}

file_line { 'PasswordAuthentication':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  match  => '^PasswordAuthentication',
}

