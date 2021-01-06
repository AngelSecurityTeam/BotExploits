#!/usr/bin/perl
#Coded By Wissem Mahfoud.
#RECORDED? Only Changed And Delete COPYRIGHT? Don't Be A Bastard Dude! if u change or edit it u are fucking idiot and kids.
#I'am a creative genius.
use if $^O eq "MSWin32",Win32::Console::ANSI;
use Digest::MD5 qw(md5 md5_hex md5_base64);
use WWW::Mechanize;
use Getopt::Long;
use HTTP::Request;
use LWP::UserAgent;
use IO::Select;
use HTTP::Cookies;
use HTTP::Response;
use Term::ANSIColor;
use HTTP::Request::Common qw(POST);
use HTTP::Request::Common qw(GET);
use MIME::Base64;
use URI::URL;
use IO::Socket::INET;
use threads;
use threads::shared;
use Thread qw(:DEFAULT async yield);
my $now_string = localtime();
@months = qw(01 02 03 04 05 06 07 08 09 10 11 12);
($second, $minute, $hour, $dayOfMonth, $month, $yearOffset, $dayOfWeek, $dayOfYear, $daylightSavings) = localtime();
$year = 1900 + $yearOffset;
$month = "$months[$month]";


system("2.py");
