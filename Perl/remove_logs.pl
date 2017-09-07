use strict;
use warnings;
use POSIX qw(strftime);

my $datestring = strftime "%Y%m", gmtime;

sub remove_unwanted_logs {
        my $p = $_[0];

        opendir(DIR, $p) or die $!;
        my @files = readdir(DIR);
        closedir(DIR);

        foreach (@files){
                if ($_ =~ m/$datestring/){
                        print "kept $_ \n";
                }else{
                        unlink"$p/$_" or warn "Could not delete file! \n";
                        print "deleting $_\n";
                }
        }
}

remove_unwanted_logs("/your/path/here");
