# Using Puppet, to fix ulimit (Max Open FIles Limit) for Nginx on Ubuntu
exec {'fix-ulimit':
  path    => '/bin/',
  command => 'sed -i s/15/1000/ /etc/default/nginx',
}
-> exec {'restart nginx service':
  path    => '/bin/',
  command => 'service nginx restart',
}
