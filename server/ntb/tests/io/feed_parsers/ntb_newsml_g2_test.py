# -*- coding: utf-8; -*-
#
# This file is part of Superdesk.
#
# Copyright 2013 - 2018 Sourcefabric z.u. and contributors.
#
# For the full copyright and license information, please see the
# AUTHORS and LICENSE files distributed with this source code, or
# at https://www.sourcefabric.org/superdesk/license


from ntb.io.feed_parsers.ntb_newsml import NTBNewsMLTwoFeedParser
from . import XMLParserTestCase


class BaseNTBNewsML2TestCase(XMLParserTestCase):
    def setUp(self):
        self.parser = NTBNewsMLTwoFeedParser()
        super().setUp()


class NTBNewsML2TestCase(BaseNTBNewsML2TestCase):
    filename = "ntb_newsml_g2.xml"

    def test_can_parse(self):
        self.assertTrue(self.parser.can_parse(self.xml_root))

    def test_content(self):
        item = self.item[0]
        self.assertEqual(item['version'], '2')
        self.assertEqual(item['subject'], [{'name': 'Utenriks', 'qcode': 'Utenriks', 'scheme': 'category'}])
        self.assertEqual(item['anpa_category'], [{'name': 'Nyhetstjenesten', 'qcode': 'n'}])
        self.assertEqual(item['headline'], 'Nutrisystem beats 4Q earnings and revenue expectations')
        self.assertEqual(item['slugline'], '')
        self.assertEqual(item['body_html'], '<p>FORT WASHINGTON, Pa. (AP) _ Nutrisystem Inc. (NTRI) on Monday reported'
                                            ' fourth-quarter net income of $10.9 million.</p>\n              \n<p>On a'
                                            ' per-share basis, the Fort Washington, Pennsylvania-based company said it'
                                            ' had profit of 36 cents. Earnings, adjusted for non-recurring costs, were'
                                            ' 42 cents per share.</p>\n              \n<p>The results beat Wall Street'
                                            ' expectations. The average estimate of four analysts surveyed by Zacks In'
                                            'vestment Research was for earnings of 41 cents per share.</p>\n          '
                                            '    \n<p>The weight-loss company posted revenue of $131.2 million in the '
                                            'period, also exceeding Street forecasts. Four analysts surveyed by Zacks '
                                            'expected $129.1 million.</p>\n              \n<p>For the year, the compan'
                                            'y reported profit of $57.9 million, or $1.90 per share. Revenue was repor'
                                            'ted as $697 million.</p>\n              \n<p>For the current quarter endi'
                                            'ng in April, Nutrisystem said it expects revenue in the range of $204 mil'
                                            'lion to $209 million.</p>\n              \n<p>The company expects full-ye'
                                            'ar earnings to be $1.99 to $2.09 per share, with revenue ranging from $68'
                                            '5 million to $705 million.</p>\n              \n<p>Nutrisystem shares hav'
                                            'e decreased 24 percent since the beginning of the year. In the final minu'
                                            'tes of trading on Monday, shares hit $39.90, a climb of almost 5 percent '
                                            'in the last 12 months.</p>\n              \n<p>_____</p>\n              '
                                            '\n<p>This story was generated by Automated Insights (http://automatedinsig'
                                            'hts.com/ap) using data from Zacks Investment Research. Access a Zacks sto'
                                            'ck report on NTRI at https://www.zacks.com/ap/NTRI</p>\n            ')
        self.assertEqual(item['guid'], 'tag:ap.org,2011:5e565888b587889c5c8bd62b6164118c-text:2')
        self.assertEqual(item['firstcreated'].isoformat(), '2018-02-26T21:20:36+00:00')
        self.assertEqual(item['urgency'], 5)
