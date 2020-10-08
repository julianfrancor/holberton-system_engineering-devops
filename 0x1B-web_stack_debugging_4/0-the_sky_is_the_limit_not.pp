# Using Puppet, to fix ulimit (Max Open FIles Limit) for Nginx on Ubuntu
exec {'fix-ulimit':
  path    => '/usr/bin/env',
  command => 'sed -i s/15/1000/ /etc/default/nginx',
}
-> exec {'restart nginx service':
  path    => '/usr/bin/env',
  command => 'service nginx restart',
}
