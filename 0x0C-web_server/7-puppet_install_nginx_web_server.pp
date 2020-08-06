
# install the package
package { 'nginx':
  ensure   => 'latest',
  name     => 'nginx',
  provider => 'apt'
}

file { 'index.html'
  path    => '/var/www/html/index.nginx-debian.html',
  mode    => '0644',
  content => 'Holberton School'
}

file_line { '301 Moved Permanently':
  path  => '/etc/nginx/sites-available/default',
  line  => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  match => '^server {'
}

service { 'nginx'
  ensure => running,
  enable => true
}
