# install the package

exec { 'update':
  command => 'sudo apt-get update',
  path    => ['/bin', '/usr/bin'],
}

package { 'nginx':
  ensure   => 'installed',
  name     => 'nginx',
  provider => 'apt'
  require  => Exec['update']
}

file_line { 'add_custom_header':
  path  => '/etc/nginx/sites-available/default',
  line  => '\tadd_header X-Served-By \$HOSTNAME;',
  after => 'server_name _;'
  require  => Exec['nginx']
}

exec { 'restart':
  command => 'sudo service nginx restart',
  path    => ['/bin', '/usr/bin'],
  require => Exec['add_custom_header']
}
