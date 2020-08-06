
# install the package
package { 'nginx':
  ensure   => 'latest',
  name     => 'nginx',
  provider => 'apt'
}

file { 'index.html':
  path    => '/var/www/html/index.nginx-debian.html',
  mode    => '0644',
  content => 'Holberton School'
}

file_line { '301 Moved Permanently':
  path  => '/etc/nginx/sites-available/default',
  line  => "\tlocation /redirect_me {\n\t\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;/n/t%7D",
  after => '^server {'
}

service { 'nginx'
  ensure => running,
  enable => true
}
