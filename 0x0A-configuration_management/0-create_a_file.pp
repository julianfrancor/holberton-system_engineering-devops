# Manifest to Create a file in puppet

file { 'holberton':                 # file resource name
  path    => '/tmp/holberton',         # destination path
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
