# install the package

exec { 'update':
  command => 'sudo apt-get update',
  path    => ['/bin', '/usr/bin'],
}

package { 'nginx':
  ensure   => 'installed',
  name     => 'nginx',
}

file_line { 'add_custom_header':
  path  => '/etc/nginx/sites-available/default',
  line  => 'add_header X-Served-By \$HOSTNAME;',
  after => '^server_name _;'
}

exec { 'restart':
  command => 'sudo service nginx restart',
  path    => ['/bin', '/usr/bin'],
}
