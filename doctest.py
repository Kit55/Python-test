<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en-US">
<head>
<link rel="icon" href="/cpython/static/hgicon.png" type="image/png" />
<meta name="robots" content="index, nofollow" />
<link rel="stylesheet" href="/cpython/static/style-paper.css" type="text/css" />
<script type="text/javascript" src="/cpython/static/mercurial.js"></script>

<link rel="stylesheet" href="/cpython/highlightcss" type="text/css" />
<title>cpython: c6880edaf6f3 Lib/doctest.py</title>
</head>
<body>

<div class="container">
<div class="menu">
<div class="logo">
<a href="https://hg.python.org">
<img src="/cpython/static/hglogo.png" alt="back to hg.python.org repositories" /></a>
</div>
<ul>
<li><a href="/cpython/shortlog/c6880edaf6f3">log</a></li>
<li><a href="/cpython/graph/c6880edaf6f3">graph</a></li>
<li><a href="/cpython/tags">tags</a></li>
<li><a href="/cpython/bookmarks">bookmarks</a></li>
<li><a href="/cpython/branches">branches</a></li>
</ul>
<ul>
<li><a href="/cpython/rev/c6880edaf6f3">changeset</a></li>
<li><a href="/cpython/file/c6880edaf6f3/Lib/">browse</a></li>
</ul>
<ul>
<li class="active">file</li>
<li><a href="/cpython/file/tip/Lib/doctest.py">latest</a></li>
<li><a href="/cpython/diff/c6880edaf6f3/Lib/doctest.py">diff</a></li>
<li><a href="/cpython/comparison/c6880edaf6f3/Lib/doctest.py">comparison</a></li>
<li><a href="/cpython/annotate/c6880edaf6f3/Lib/doctest.py">annotate</a></li>
<li><a href="/cpython/log/c6880edaf6f3/Lib/doctest.py">file log</a></li>
<li><a href="/cpython/raw-file/c6880edaf6f3/Lib/doctest.py">raw</a></li>
</ul>
<ul>
<li><a href="/cpython/help">help</a></li>
</ul>
</div>

<div class="main">
<h2 class="breadcrumb"><a href="/">Mercurial</a> &gt; <a href="/cpython">cpython</a> </h2>
<h3>
 view Lib/doctest.py @ 74131:<a href="/cpython/rev/c6880edaf6f3">c6880edaf6f3</a>
 <span class="branchname">2.7</span> 
</h3>

<form class="search" action="/cpython/log">

<p><input name="rev" id="search1" type="text" size="30" /></p>
<div id="hint">Find changesets by keywords (author, files, the commit message), revision
number or hash, or <a href="/cpython/help/revsets">revset expression</a>.</div>
</form>

<div class="description">Issue13443 - Remove the functional module examples from 2.7 (as module is
maintained only till 2.5 and tests had failures with 2.7) and update the links
int the howto document.</div>

<table id="changesetEntry">
<tr>
 <th class="author">author</th>
 <td class="author">&#83;&#101;&#110;&#116;&#104;&#105;&#108;&#32;&#75;&#117;&#109;&#97;&#114;&#97;&#110;&#32;&#60;&#115;&#101;&#110;&#116;&#104;&#105;&#108;&#64;&#117;&#116;&#104;&#99;&#111;&#100;&#101;&#46;&#99;&#111;&#109;&#62;</td>
</tr>
<tr>
 <th class="date">date</th>
 <td class="date age">Thu, 22 Dec 2011 23:44:53 +0800</td>
</tr>
<tr>
 <th class="author">parents</th>
 <td class="author"><a href="/cpython/file/6a95820b9607/Lib/doctest.py">6a95820b9607</a> </td>
</tr>
<tr>
 <th class="author">children</th>
 <td class="author"><a href="/cpython/file/c50db3d06116/Lib/doctest.py">c50db3d06116</a> </td>
</tr>
</table>

<div class="overflow">
<div class="sourcefirst linewraptoggle">line wrap: <a class="linewraplink" href="javascript:toggleLinewrap()">on</a></div>
<div class="sourcefirst"> line source</div>
<pre class="sourcelines stripes4 wrap">
<span id="l1"><span class="c"># Module doctest.</span></span><a href="#l1"></a>
<span id="l2"><span class="c"># Released to the public domain 16-Jan-2001, by Tim Peters (tim@python.org).</span></span><a href="#l2"></a>
<span id="l3"><span class="c"># Major enhancements and refactoring by:</span></span><a href="#l3"></a>
<span id="l4"><span class="c">#     Jim Fulton</span></span><a href="#l4"></a>
<span id="l5"><span class="c">#     Edward Loper</span></span><a href="#l5"></a>
<span id="l6"></span><a href="#l6"></a>
<span id="l7"><span class="c"># Provided as-is; use at your own risk; no warranty; no promises; enjoy!</span></span><a href="#l7"></a>
<span id="l8"></span><a href="#l8"></a>
<span id="l9"><span class="sd">r&quot;&quot;&quot;Module doctest -- a framework for running examples in docstrings.</span></span><a href="#l9"></a>
<span id="l10"></span><a href="#l10"></a>
<span id="l11"><span class="sd">In simplest use, end each module M to be tested with:</span></span><a href="#l11"></a>
<span id="l12"></span><a href="#l12"></a>
<span id="l13"><span class="sd">def _test():</span></span><a href="#l13"></a>
<span id="l14"><span class="sd">    import doctest</span></span><a href="#l14"></a>
<span id="l15"><span class="sd">    doctest.testmod()</span></span><a href="#l15"></a>
<span id="l16"></span><a href="#l16"></a>
<span id="l17"><span class="sd">if __name__ == &quot;__main__&quot;:</span></span><a href="#l17"></a>
<span id="l18"><span class="sd">    _test()</span></span><a href="#l18"></a>
<span id="l19"></span><a href="#l19"></a>
<span id="l20"><span class="sd">Then running the module as a script will cause the examples in the</span></span><a href="#l20"></a>
<span id="l21"><span class="sd">docstrings to get executed and verified:</span></span><a href="#l21"></a>
<span id="l22"></span><a href="#l22"></a>
<span id="l23"><span class="sd">python M.py</span></span><a href="#l23"></a>
<span id="l24"></span><a href="#l24"></a>
<span id="l25"><span class="sd">This won&#39;t display anything unless an example fails, in which case the</span></span><a href="#l25"></a>
<span id="l26"><span class="sd">failing example(s) and the cause(s) of the failure(s) are printed to stdout</span></span><a href="#l26"></a>
<span id="l27"><span class="sd">(why not stderr? because stderr is a lame hack &lt;0.2 wink&gt;), and the final</span></span><a href="#l27"></a>
<span id="l28"><span class="sd">line of output is &quot;Test failed.&quot;.</span></span><a href="#l28"></a>
<span id="l29"></span><a href="#l29"></a>
<span id="l30"><span class="sd">Run it with the -v switch instead:</span></span><a href="#l30"></a>
<span id="l31"></span><a href="#l31"></a>
<span id="l32"><span class="sd">python M.py -v</span></span><a href="#l32"></a>
<span id="l33"></span><a href="#l33"></a>
<span id="l34"><span class="sd">and a detailed report of all examples tried is printed to stdout, along</span></span><a href="#l34"></a>
<span id="l35"><span class="sd">with assorted summaries at the end.</span></span><a href="#l35"></a>
<span id="l36"></span><a href="#l36"></a>
<span id="l37"><span class="sd">You can force verbose mode by passing &quot;verbose=True&quot; to testmod, or prohibit</span></span><a href="#l37"></a>
<span id="l38"><span class="sd">it by passing &quot;verbose=False&quot;.  In either of those cases, sys.argv is not</span></span><a href="#l38"></a>
<span id="l39"><span class="sd">examined by testmod.</span></span><a href="#l39"></a>
<span id="l40"></span><a href="#l40"></a>
<span id="l41"><span class="sd">There are a variety of other ways to run doctests, including integration</span></span><a href="#l41"></a>
<span id="l42"><span class="sd">with the unittest framework, and support for running non-Python text</span></span><a href="#l42"></a>
<span id="l43"><span class="sd">files containing doctests.  There are also many ways to override parts</span></span><a href="#l43"></a>
<span id="l44"><span class="sd">of doctest&#39;s default behaviors.  See the Library Reference Manual for</span></span><a href="#l44"></a>
<span id="l45"><span class="sd">details.</span></span><a href="#l45"></a>
<span id="l46"><span class="sd">&quot;&quot;&quot;</span></span><a href="#l46"></a>
<span id="l47"></span><a href="#l47"></a>
<span id="l48"><span class="n">__docformat__</span> <span class="o">=</span> <span class="s">&#39;reStructuredText en&#39;</span></span><a href="#l48"></a>
<span id="l49"></span><a href="#l49"></a>
<span id="l50"><span class="n">__all__</span> <span class="o">=</span> <span class="p">[</span></span><a href="#l50"></a>
<span id="l51">    <span class="c"># 0, Option Flags</span></span><a href="#l51"></a>
<span id="l52">    <span class="s">&#39;register_optionflag&#39;</span><span class="p">,</span></span><a href="#l52"></a>
<span id="l53">    <span class="s">&#39;DONT_ACCEPT_TRUE_FOR_1&#39;</span><span class="p">,</span></span><a href="#l53"></a>
<span id="l54">    <span class="s">&#39;DONT_ACCEPT_BLANKLINE&#39;</span><span class="p">,</span></span><a href="#l54"></a>
<span id="l55">    <span class="s">&#39;NORMALIZE_WHITESPACE&#39;</span><span class="p">,</span></span><a href="#l55"></a>
<span id="l56">    <span class="s">&#39;ELLIPSIS&#39;</span><span class="p">,</span></span><a href="#l56"></a>
<span id="l57">    <span class="s">&#39;SKIP&#39;</span><span class="p">,</span></span><a href="#l57"></a>
<span id="l58">    <span class="s">&#39;IGNORE_EXCEPTION_DETAIL&#39;</span><span class="p">,</span></span><a href="#l58"></a>
<span id="l59">    <span class="s">&#39;COMPARISON_FLAGS&#39;</span><span class="p">,</span></span><a href="#l59"></a>
<span id="l60">    <span class="s">&#39;REPORT_UDIFF&#39;</span><span class="p">,</span></span><a href="#l60"></a>
<span id="l61">    <span class="s">&#39;REPORT_CDIFF&#39;</span><span class="p">,</span></span><a href="#l61"></a>
<span id="l62">    <span class="s">&#39;REPORT_NDIFF&#39;</span><span class="p">,</span></span><a href="#l62"></a>
<span id="l63">    <span class="s">&#39;REPORT_ONLY_FIRST_FAILURE&#39;</span><span class="p">,</span></span><a href="#l63"></a>
<span id="l64">    <span class="s">&#39;REPORTING_FLAGS&#39;</span><span class="p">,</span></span><a href="#l64"></a>
<span id="l65">    <span class="c"># 1. Utility Functions</span></span><a href="#l65"></a>
<span id="l66">    <span class="c"># 2. Example &amp; DocTest</span></span><a href="#l66"></a>
<span id="l67">    <span class="s">&#39;Example&#39;</span><span class="p">,</span></span><a href="#l67"></a>
<span id="l68">    <span class="s">&#39;DocTest&#39;</span><span class="p">,</span></span><a href="#l68"></a>
<span id="l69">    <span class="c"># 3. Doctest Parser</span></span><a href="#l69"></a>
<span id="l70">    <span class="s">&#39;DocTestParser&#39;</span><span class="p">,</span></span><a href="#l70"></a>
<span id="l71">    <span class="c"># 4. Doctest Finder</span></span><a href="#l71"></a>
<span id="l72">    <span class="s">&#39;DocTestFinder&#39;</span><span class="p">,</span></span><a href="#l72"></a>
<span id="l73">    <span class="c"># 5. Doctest Runner</span></span><a href="#l73"></a>
<span id="l74">    <span class="s">&#39;DocTestRunner&#39;</span><span class="p">,</span></span><a href="#l74"></a>
<span id="l75">    <span class="s">&#39;OutputChecker&#39;</span><span class="p">,</span></span><a href="#l75"></a>
<span id="l76">    <span class="s">&#39;DocTestFailure&#39;</span><span class="p">,</span></span><a href="#l76"></a>
<span id="l77">    <span class="s">&#39;UnexpectedException&#39;</span><span class="p">,</span></span><a href="#l77"></a>
<span id="l78">    <span class="s">&#39;DebugRunner&#39;</span><span class="p">,</span></span><a href="#l78"></a>
<span id="l79">    <span class="c"># 6. Test Functions</span></span><a href="#l79"></a>
<span id="l80">    <span class="s">&#39;testmod&#39;</span><span class="p">,</span></span><a href="#l80"></a>
<span id="l81">    <span class="s">&#39;testfile&#39;</span><span class="p">,</span></span><a href="#l81"></a>
<span id="l82">    <span class="s">&#39;run_docstring_examples&#39;</span><span class="p">,</span></span><a href="#l82"></a>
<span id="l83">    <span class="c"># 7. Tester</span></span><a href="#l83"></a>
<span id="l84">    <span class="s">&#39;Tester&#39;</span><span class="p">,</span></span><a href="#l84"></a>
<span id="l85">    <span class="c"># 8. Unittest Support</span></span><a href="#l85"></a>
<span id="l86">    <span class="s">&#39;DocTestSuite&#39;</span><span class="p">,</span></span><a href="#l86"></a>
<span id="l87">    <span class="s">&#39;DocFileSuite&#39;</span><span class="p">,</span></span><a href="#l87"></a>
<span id="l88">    <span class="s">&#39;set_unittest_reportflags&#39;</span><span class="p">,</span></span><a href="#l88"></a>
<span id="l89">    <span class="c"># 9. Debugging Support</span></span><a href="#l89"></a>
<span id="l90">    <span class="s">&#39;script_from_examples&#39;</span><span class="p">,</span></span><a href="#l90"></a>
<span id="l91">    <span class="s">&#39;testsource&#39;</span><span class="p">,</span></span><a href="#l91"></a>
<span id="l92">    <span class="s">&#39;debug_src&#39;</span><span class="p">,</span></span><a href="#l92"></a>
<span id="l93">    <span class="s">&#39;debug&#39;</span><span class="p">,</span></span><a href="#l93"></a>
<span id="l94"><span class="p">]</span></span><a href="#l94"></a>
<span id="l95"></span><a href="#l95"></a>
<span id="l96"><span class="kn">import</span> <span class="nn">__future__</span></span><a href="#l96"></a>
<span id="l97"></span><a href="#l97"></a>
<span id="l98"><span class="kn">import</span> <span class="nn">sys</span><span class="o">,</span> <span class="nn">traceback</span><span class="o">,</span> <span class="nn">inspect</span><span class="o">,</span> <span class="nn">linecache</span><span class="o">,</span> <span class="nn">os</span><span class="o">,</span> <span class="nn">re</span></span><a href="#l98"></a>
<span id="l99"><span class="kn">import</span> <span class="nn">unittest</span><span class="o">,</span> <span class="nn">difflib</span><span class="o">,</span> <span class="nn">pdb</span><span class="o">,</span> <span class="nn">tempfile</span></span><a href="#l99"></a>
<span id="l100"><span class="kn">import</span> <span class="nn">warnings</span></span><a href="#l100"></a>
<span id="l101"><span class="kn">from</span> <span class="nn">StringIO</span> <span class="kn">import</span> <span class="n">StringIO</span></span><a href="#l101"></a>
<span id="l102"><span class="kn">from</span> <span class="nn">collections</span> <span class="kn">import</span> <span class="n">namedtuple</span></span><a href="#l102"></a>
<span id="l103"></span><a href="#l103"></a>
<span id="l104"><span class="n">TestResults</span> <span class="o">=</span> <span class="n">namedtuple</span><span class="p">(</span><span class="s">&#39;TestResults&#39;</span><span class="p">,</span> <span class="s">&#39;failed attempted&#39;</span><span class="p">)</span></span><a href="#l104"></a>
<span id="l105"></span><a href="#l105"></a>
<span id="l106"><span class="c"># There are 4 basic classes:</span></span><a href="#l106"></a>
<span id="l107"><span class="c">#  - Example: a &lt;source, want&gt; pair, plus an intra-docstring line number.</span></span><a href="#l107"></a>
<span id="l108"><span class="c">#  - DocTest: a collection of examples, parsed from a docstring, plus</span></span><a href="#l108"></a>
<span id="l109"><span class="c">#    info about where the docstring came from (name, filename, lineno).</span></span><a href="#l109"></a>
<span id="l110"><span class="c">#  - DocTestFinder: extracts DocTests from a given object&#39;s docstring and</span></span><a href="#l110"></a>
<span id="l111"><span class="c">#    its contained objects&#39; docstrings.</span></span><a href="#l111"></a>
<span id="l112"><span class="c">#  - DocTestRunner: runs DocTest cases, and accumulates statistics.</span></span><a href="#l112"></a>
<span id="l113"><span class="c">#</span></span><a href="#l113"></a>
<span id="l114"><span class="c"># So the basic picture is:</span></span><a href="#l114"></a>
<span id="l115"><span class="c">#</span></span><a href="#l115"></a>
<span id="l116"><span class="c">#                             list of:</span></span><a href="#l116"></a>
<span id="l117"><span class="c"># +------+                   +---------+                   +-------+</span></span><a href="#l117"></a>
<span id="l118"><span class="c"># |object| --DocTestFinder-&gt; | DocTest | --DocTestRunner-&gt; |results|</span></span><a href="#l118"></a>
<span id="l119"><span class="c"># +------+                   +---------+                   +-------+</span></span><a href="#l119"></a>
<span id="l120"><span class="c">#                            | Example |</span></span><a href="#l120"></a>
<span id="l121"><span class="c">#                            |   ...   |</span></span><a href="#l121"></a>
<span id="l122"><span class="c">#                            | Example |</span></span><a href="#l122"></a>
<span id="l123"><span class="c">#                            +---------+</span></span><a href="#l123"></a>
<span id="l124"></span><a href="#l124"></a>
<span id="l125"><span class="c"># Option constants.</span></span><a href="#l125"></a>
<span id="l126"></span><a href="#l126"></a>
<span id="l127"><span class="n">OPTIONFLAGS_BY_NAME</span> <span class="o">=</span> <span class="p">{}</span></span><a href="#l127"></a>
<span id="l128"><span class="k">def</span> <span class="nf">register_optionflag</span><span class="p">(</span><span class="n">name</span><span class="p">):</span></span><a href="#l128"></a>
<span id="l129">    <span class="c"># Create a new flag unless `name` is already known.</span></span><a href="#l129"></a>
<span id="l130">    <span class="k">return</span> <span class="n">OPTIONFLAGS_BY_NAME</span><span class="o">.</span><span class="n">setdefault</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="mi">1</span> <span class="o">&lt;&lt;</span> <span class="nb">len</span><span class="p">(</span><span class="n">OPTIONFLAGS_BY_NAME</span><span class="p">))</span></span><a href="#l130"></a>
<span id="l131"></span><a href="#l131"></a>
<span id="l132"><span class="n">DONT_ACCEPT_TRUE_FOR_1</span> <span class="o">=</span> <span class="n">register_optionflag</span><span class="p">(</span><span class="s">&#39;DONT_ACCEPT_TRUE_FOR_1&#39;</span><span class="p">)</span></span><a href="#l132"></a>
<span id="l133"><span class="n">DONT_ACCEPT_BLANKLINE</span> <span class="o">=</span> <span class="n">register_optionflag</span><span class="p">(</span><span class="s">&#39;DONT_ACCEPT_BLANKLINE&#39;</span><span class="p">)</span></span><a href="#l133"></a>
<span id="l134"><span class="n">NORMALIZE_WHITESPACE</span> <span class="o">=</span> <span class="n">register_optionflag</span><span class="p">(</span><span class="s">&#39;NORMALIZE_WHITESPACE&#39;</span><span class="p">)</span></span><a href="#l134"></a>
<span id="l135"><span class="n">ELLIPSIS</span> <span class="o">=</span> <span class="n">register_optionflag</span><span class="p">(</span><span class="s">&#39;ELLIPSIS&#39;</span><span class="p">)</span></span><a href="#l135"></a>
<span id="l136"><span class="n">SKIP</span> <span class="o">=</span> <span class="n">register_optionflag</span><span class="p">(</span><span class="s">&#39;SKIP&#39;</span><span class="p">)</span></span><a href="#l136"></a>
<span id="l137"><span class="n">IGNORE_EXCEPTION_DETAIL</span> <span class="o">=</span> <span class="n">register_optionflag</span><span class="p">(</span><span class="s">&#39;IGNORE_EXCEPTION_DETAIL&#39;</span><span class="p">)</span></span><a href="#l137"></a>
<span id="l138"></span><a href="#l138"></a>
<span id="l139"><span class="n">COMPARISON_FLAGS</span> <span class="o">=</span> <span class="p">(</span><span class="n">DONT_ACCEPT_TRUE_FOR_1</span> <span class="o">|</span></span><a href="#l139"></a>
<span id="l140">                    <span class="n">DONT_ACCEPT_BLANKLINE</span> <span class="o">|</span></span><a href="#l140"></a>
<span id="l141">                    <span class="n">NORMALIZE_WHITESPACE</span> <span class="o">|</span></span><a href="#l141"></a>
<span id="l142">                    <span class="n">ELLIPSIS</span> <span class="o">|</span></span><a href="#l142"></a>
<span id="l143">                    <span class="n">SKIP</span> <span class="o">|</span></span><a href="#l143"></a>
<span id="l144">                    <span class="n">IGNORE_EXCEPTION_DETAIL</span><span class="p">)</span></span><a href="#l144"></a>
<span id="l145"></span><a href="#l145"></a>
<span id="l146"><span class="n">REPORT_UDIFF</span> <span class="o">=</span> <span class="n">register_optionflag</span><span class="p">(</span><span class="s">&#39;REPORT_UDIFF&#39;</span><span class="p">)</span></span><a href="#l146"></a>
<span id="l147"><span class="n">REPORT_CDIFF</span> <span class="o">=</span> <span class="n">register_optionflag</span><span class="p">(</span><span class="s">&#39;REPORT_CDIFF&#39;</span><span class="p">)</span></span><a href="#l147"></a>
<span id="l148"><span class="n">REPORT_NDIFF</span> <span class="o">=</span> <span class="n">register_optionflag</span><span class="p">(</span><span class="s">&#39;REPORT_NDIFF&#39;</span><span class="p">)</span></span><a href="#l148"></a>
<span id="l149"><span class="n">REPORT_ONLY_FIRST_FAILURE</span> <span class="o">=</span> <span class="n">register_optionflag</span><span class="p">(</span><span class="s">&#39;REPORT_ONLY_FIRST_FAILURE&#39;</span><span class="p">)</span></span><a href="#l149"></a>
<span id="l150"></span><a href="#l150"></a>
<span id="l151"><span class="n">REPORTING_FLAGS</span> <span class="o">=</span> <span class="p">(</span><span class="n">REPORT_UDIFF</span> <span class="o">|</span></span><a href="#l151"></a>
<span id="l152">                   <span class="n">REPORT_CDIFF</span> <span class="o">|</span></span><a href="#l152"></a>
<span id="l153">                   <span class="n">REPORT_NDIFF</span> <span class="o">|</span></span><a href="#l153"></a>
<span id="l154">                   <span class="n">REPORT_ONLY_FIRST_FAILURE</span><span class="p">)</span></span><a href="#l154"></a>
<span id="l155"></span><a href="#l155"></a>
<span id="l156"><span class="c"># Special string markers for use in `want` strings:</span></span><a href="#l156"></a>
<span id="l157"><span class="n">BLANKLINE_MARKER</span> <span class="o">=</span> <span class="s">&#39;&lt;BLANKLINE&gt;&#39;</span></span><a href="#l157"></a>
<span id="l158"><span class="n">ELLIPSIS_MARKER</span> <span class="o">=</span> <span class="s">&#39;...&#39;</span></span><a href="#l158"></a>
<span id="l159"></span><a href="#l159"></a>
<span id="l160"><span class="c">######################################################################</span></span><a href="#l160"></a>
<span id="l161"><span class="c">## Table of Contents</span></span><a href="#l161"></a>
<span id="l162"><span class="c">######################################################################</span></span><a href="#l162"></a>
<span id="l163"><span class="c">#  1. Utility Functions</span></span><a href="#l163"></a>
<span id="l164"><span class="c">#  2. Example &amp; DocTest -- store test cases</span></span><a href="#l164"></a>
<span id="l165"><span class="c">#  3. DocTest Parser -- extracts examples from strings</span></span><a href="#l165"></a>
<span id="l166"><span class="c">#  4. DocTest Finder -- extracts test cases from objects</span></span><a href="#l166"></a>
<span id="l167"><span class="c">#  5. DocTest Runner -- runs test cases</span></span><a href="#l167"></a>
<span id="l168"><span class="c">#  6. Test Functions -- convenient wrappers for testing</span></span><a href="#l168"></a>
<span id="l169"><span class="c">#  7. Tester Class -- for backwards compatibility</span></span><a href="#l169"></a>
<span id="l170"><span class="c">#  8. Unittest Support</span></span><a href="#l170"></a>
<span id="l171"><span class="c">#  9. Debugging Support</span></span><a href="#l171"></a>
<span id="l172"><span class="c"># 10. Example Usage</span></span><a href="#l172"></a>
<span id="l173"></span><a href="#l173"></a>
<span id="l174"><span class="c">######################################################################</span></span><a href="#l174"></a>
<span id="l175"><span class="c">## 1. Utility Functions</span></span><a href="#l175"></a>
<span id="l176"><span class="c">######################################################################</span></span><a href="#l176"></a>
<span id="l177"></span><a href="#l177"></a>
<span id="l178"><span class="k">def</span> <span class="nf">_extract_future_flags</span><span class="p">(</span><span class="n">globs</span><span class="p">):</span></span><a href="#l178"></a>
<span id="l179">    <span class="sd">&quot;&quot;&quot;</span></span><a href="#l179"></a>
<span id="l180"><span class="sd">    Return the compiler-flags associated with the future features that</span></span><a href="#l180"></a>
<span id="l181"><span class="sd">    have been imported into the given namespace (globs).</span></span><a href="#l181"></a>
<span id="l182"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l182"></a>
<span id="l183">    <span class="n">flags</span> <span class="o">=</span> <span class="mi">0</span></span><a href="#l183"></a>
<span id="l184">    <span class="k">for</span> <span class="n">fname</span> <span class="ow">in</span> <span class="n">__future__</span><span class="o">.</span><span class="n">all_feature_names</span><span class="p">:</span></span><a href="#l184"></a>
<span id="l185">        <span class="n">feature</span> <span class="o">=</span> <span class="n">globs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">fname</span><span class="p">,</span> <span class="bp">None</span><span class="p">)</span></span><a href="#l185"></a>
<span id="l186">        <span class="k">if</span> <span class="n">feature</span> <span class="ow">is</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">__future__</span><span class="p">,</span> <span class="n">fname</span><span class="p">):</span></span><a href="#l186"></a>
<span id="l187">            <span class="n">flags</span> <span class="o">|=</span> <span class="n">feature</span><span class="o">.</span><span class="n">compiler_flag</span></span><a href="#l187"></a>
<span id="l188">    <span class="k">return</span> <span class="n">flags</span></span><a href="#l188"></a>
<span id="l189"></span><a href="#l189"></a>
<span id="l190"><span class="k">def</span> <span class="nf">_normalize_module</span><span class="p">(</span><span class="n">module</span><span class="p">,</span> <span class="n">depth</span><span class="o">=</span><span class="mi">2</span><span class="p">):</span></span><a href="#l190"></a>
<span id="l191">    <span class="sd">&quot;&quot;&quot;</span></span><a href="#l191"></a>
<span id="l192"><span class="sd">    Return the module specified by `module`.  In particular:</span></span><a href="#l192"></a>
<span id="l193"><span class="sd">      - If `module` is a module, then return module.</span></span><a href="#l193"></a>
<span id="l194"><span class="sd">      - If `module` is a string, then import and return the</span></span><a href="#l194"></a>
<span id="l195"><span class="sd">        module with that name.</span></span><a href="#l195"></a>
<span id="l196"><span class="sd">      - If `module` is None, then return the calling module.</span></span><a href="#l196"></a>
<span id="l197"><span class="sd">        The calling module is assumed to be the module of</span></span><a href="#l197"></a>
<span id="l198"><span class="sd">        the stack frame at the given depth in the call stack.</span></span><a href="#l198"></a>
<span id="l199"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l199"></a>
<span id="l200">    <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">ismodule</span><span class="p">(</span><span class="n">module</span><span class="p">):</span></span><a href="#l200"></a>
<span id="l201">        <span class="k">return</span> <span class="n">module</span></span><a href="#l201"></a>
<span id="l202">    <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">module</span><span class="p">,</span> <span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="nb">unicode</span><span class="p">)):</span></span><a href="#l202"></a>
<span id="l203">        <span class="k">return</span> <span class="nb">__import__</span><span class="p">(</span><span class="n">module</span><span class="p">,</span> <span class="nb">globals</span><span class="p">(),</span> <span class="nb">locals</span><span class="p">(),</span> <span class="p">[</span><span class="s">&quot;*&quot;</span><span class="p">])</span></span><a href="#l203"></a>
<span id="l204">    <span class="k">elif</span> <span class="n">module</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l204"></a>
<span id="l205">        <span class="k">return</span> <span class="n">sys</span><span class="o">.</span><span class="n">modules</span><span class="p">[</span><span class="n">sys</span><span class="o">.</span><span class="n">_getframe</span><span class="p">(</span><span class="n">depth</span><span class="p">)</span><span class="o">.</span><span class="n">f_globals</span><span class="p">[</span><span class="s">&#39;__name__&#39;</span><span class="p">]]</span></span><a href="#l205"></a>
<span id="l206">    <span class="k">else</span><span class="p">:</span></span><a href="#l206"></a>
<span id="l207">        <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="s">&quot;Expected a module, string, or None&quot;</span><span class="p">)</span></span><a href="#l207"></a>
<span id="l208"></span><a href="#l208"></a>
<span id="l209"><span class="k">def</span> <span class="nf">_load_testfile</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="n">package</span><span class="p">,</span> <span class="n">module_relative</span><span class="p">):</span></span><a href="#l209"></a>
<span id="l210">    <span class="k">if</span> <span class="n">module_relative</span><span class="p">:</span></span><a href="#l210"></a>
<span id="l211">        <span class="n">package</span> <span class="o">=</span> <span class="n">_normalize_module</span><span class="p">(</span><span class="n">package</span><span class="p">,</span> <span class="mi">3</span><span class="p">)</span></span><a href="#l211"></a>
<span id="l212">        <span class="n">filename</span> <span class="o">=</span> <span class="n">_module_relative_path</span><span class="p">(</span><span class="n">package</span><span class="p">,</span> <span class="n">filename</span><span class="p">)</span></span><a href="#l212"></a>
<span id="l213">        <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">package</span><span class="p">,</span> <span class="s">&#39;__loader__&#39;</span><span class="p">):</span></span><a href="#l213"></a>
<span id="l214">            <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">package</span><span class="o">.</span><span class="n">__loader__</span><span class="p">,</span> <span class="s">&#39;get_data&#39;</span><span class="p">):</span></span><a href="#l214"></a>
<span id="l215">                <span class="n">file_contents</span> <span class="o">=</span> <span class="n">package</span><span class="o">.</span><span class="n">__loader__</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="n">filename</span><span class="p">)</span></span><a href="#l215"></a>
<span id="l216">                <span class="c"># get_data() opens files as &#39;rb&#39;, so one must do the equivalent</span></span><a href="#l216"></a>
<span id="l217">                <span class="c"># conversion as universal newlines would do.</span></span><a href="#l217"></a>
<span id="l218">                <span class="k">return</span> <span class="n">file_contents</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">linesep</span><span class="p">,</span> <span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">),</span> <span class="n">filename</span></span><a href="#l218"></a>
<span id="l219">    <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">filename</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span></span><a href="#l219"></a>
<span id="l220">        <span class="k">return</span> <span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">(),</span> <span class="n">filename</span></span><a href="#l220"></a>
<span id="l221"></span><a href="#l221"></a>
<span id="l222"><span class="c"># Use sys.stdout encoding for ouput.</span></span><a href="#l222"></a>
<span id="l223"><span class="n">_encoding</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">__stdout__</span><span class="p">,</span> <span class="s">&#39;encoding&#39;</span><span class="p">,</span> <span class="bp">None</span><span class="p">)</span> <span class="ow">or</span> <span class="s">&#39;utf-8&#39;</span></span><a href="#l223"></a>
<span id="l224"></span><a href="#l224"></a>
<span id="l225"><span class="k">def</span> <span class="nf">_indent</span><span class="p">(</span><span class="n">s</span><span class="p">,</span> <span class="n">indent</span><span class="o">=</span><span class="mi">4</span><span class="p">):</span></span><a href="#l225"></a>
<span id="l226">    <span class="sd">&quot;&quot;&quot;</span></span><a href="#l226"></a>
<span id="l227"><span class="sd">    Add the given number of space characters to the beginning of</span></span><a href="#l227"></a>
<span id="l228"><span class="sd">    every non-blank line in `s`, and return the result.</span></span><a href="#l228"></a>
<span id="l229"><span class="sd">    If the string `s` is Unicode, it is encoded using the stdout</span></span><a href="#l229"></a>
<span id="l230"><span class="sd">    encoding and the `backslashreplace` error handler.</span></span><a href="#l230"></a>
<span id="l231"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l231"></a>
<span id="l232">    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">s</span><span class="p">,</span> <span class="nb">unicode</span><span class="p">):</span></span><a href="#l232"></a>
<span id="l233">        <span class="n">s</span> <span class="o">=</span> <span class="n">s</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="n">_encoding</span><span class="p">,</span> <span class="s">&#39;backslashreplace&#39;</span><span class="p">)</span></span><a href="#l233"></a>
<span id="l234">    <span class="c"># This regexp matches the start of non-blank lines:</span></span><a href="#l234"></a>
<span id="l235">    <span class="k">return</span> <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="s">&#39;(?m)^(?!$)&#39;</span><span class="p">,</span> <span class="n">indent</span><span class="o">*</span><span class="s">&#39; &#39;</span><span class="p">,</span> <span class="n">s</span><span class="p">)</span></span><a href="#l235"></a>
<span id="l236"></span><a href="#l236"></a>
<span id="l237"><span class="k">def</span> <span class="nf">_exception_traceback</span><span class="p">(</span><span class="n">exc_info</span><span class="p">):</span></span><a href="#l237"></a>
<span id="l238">    <span class="sd">&quot;&quot;&quot;</span></span><a href="#l238"></a>
<span id="l239"><span class="sd">    Return a string containing a traceback message for the given</span></span><a href="#l239"></a>
<span id="l240"><span class="sd">    exc_info tuple (as returned by sys.exc_info()).</span></span><a href="#l240"></a>
<span id="l241"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l241"></a>
<span id="l242">    <span class="c"># Get a traceback message.</span></span><a href="#l242"></a>
<span id="l243">    <span class="n">excout</span> <span class="o">=</span> <span class="n">StringIO</span><span class="p">()</span></span><a href="#l243"></a>
<span id="l244">    <span class="n">exc_type</span><span class="p">,</span> <span class="n">exc_val</span><span class="p">,</span> <span class="n">exc_tb</span> <span class="o">=</span> <span class="n">exc_info</span></span><a href="#l244"></a>
<span id="l245">    <span class="n">traceback</span><span class="o">.</span><span class="n">print_exception</span><span class="p">(</span><span class="n">exc_type</span><span class="p">,</span> <span class="n">exc_val</span><span class="p">,</span> <span class="n">exc_tb</span><span class="p">,</span> <span class="nb">file</span><span class="o">=</span><span class="n">excout</span><span class="p">)</span></span><a href="#l245"></a>
<span id="l246">    <span class="k">return</span> <span class="n">excout</span><span class="o">.</span><span class="n">getvalue</span><span class="p">()</span></span><a href="#l246"></a>
<span id="l247"></span><a href="#l247"></a>
<span id="l248"><span class="c"># Override some StringIO methods.</span></span><a href="#l248"></a>
<span id="l249"><span class="k">class</span> <span class="nc">_SpoofOut</span><span class="p">(</span><span class="n">StringIO</span><span class="p">):</span></span><a href="#l249"></a>
<span id="l250">    <span class="k">def</span> <span class="nf">getvalue</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l250"></a>
<span id="l251">        <span class="n">result</span> <span class="o">=</span> <span class="n">StringIO</span><span class="o">.</span><span class="n">getvalue</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span></span><a href="#l251"></a>
<span id="l252">        <span class="c"># If anything at all was written, make sure there&#39;s a trailing</span></span><a href="#l252"></a>
<span id="l253">        <span class="c"># newline.  There&#39;s no way for the expected output to indicate</span></span><a href="#l253"></a>
<span id="l254">        <span class="c"># that a trailing newline is missing.</span></span><a href="#l254"></a>
<span id="l255">        <span class="k">if</span> <span class="n">result</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">result</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s">&quot;</span><span class="se">\n</span><span class="s">&quot;</span><span class="p">):</span></span><a href="#l255"></a>
<span id="l256">            <span class="n">result</span> <span class="o">+=</span> <span class="s">&quot;</span><span class="se">\n</span><span class="s">&quot;</span></span><a href="#l256"></a>
<span id="l257">        <span class="c"># Prevent softspace from screwing up the next test case, in</span></span><a href="#l257"></a>
<span id="l258">        <span class="c"># case they used print with a trailing comma in an example.</span></span><a href="#l258"></a>
<span id="l259">        <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="s">&quot;softspace&quot;</span><span class="p">):</span></span><a href="#l259"></a>
<span id="l260">            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">softspace</span></span><a href="#l260"></a>
<span id="l261">        <span class="k">return</span> <span class="n">result</span></span><a href="#l261"></a>
<span id="l262"></span><a href="#l262"></a>
<span id="l263">    <span class="k">def</span> <span class="nf">truncate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span>   <span class="n">size</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l263"></a>
<span id="l264">        <span class="n">StringIO</span><span class="o">.</span><span class="n">truncate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">size</span><span class="p">)</span></span><a href="#l264"></a>
<span id="l265">        <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="s">&quot;softspace&quot;</span><span class="p">):</span></span><a href="#l265"></a>
<span id="l266">            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">softspace</span></span><a href="#l266"></a>
<span id="l267">        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">buf</span><span class="p">:</span></span><a href="#l267"></a>
<span id="l268">            <span class="c"># Reset it to an empty string, to make sure it&#39;s not unicode.</span></span><a href="#l268"></a>
<span id="l269">            <span class="bp">self</span><span class="o">.</span><span class="n">buf</span> <span class="o">=</span> <span class="s">&#39;&#39;</span></span><a href="#l269"></a>
<span id="l270"></span><a href="#l270"></a>
<span id="l271"><span class="c"># Worst-case linear-time ellipsis matching.</span></span><a href="#l271"></a>
<span id="l272"><span class="k">def</span> <span class="nf">_ellipsis_match</span><span class="p">(</span><span class="n">want</span><span class="p">,</span> <span class="n">got</span><span class="p">):</span></span><a href="#l272"></a>
<span id="l273">    <span class="sd">&quot;&quot;&quot;</span></span><a href="#l273"></a>
<span id="l274"><span class="sd">    Essentially the only subtle case:</span></span><a href="#l274"></a>
<span id="l275"><span class="sd">    &gt;&gt;&gt; _ellipsis_match(&#39;aa...aa&#39;, &#39;aaa&#39;)</span></span><a href="#l275"></a>
<span id="l276"><span class="sd">    False</span></span><a href="#l276"></a>
<span id="l277"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l277"></a>
<span id="l278">    <span class="k">if</span> <span class="n">ELLIPSIS_MARKER</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">want</span><span class="p">:</span></span><a href="#l278"></a>
<span id="l279">        <span class="k">return</span> <span class="n">want</span> <span class="o">==</span> <span class="n">got</span></span><a href="#l279"></a>
<span id="l280"></span><a href="#l280"></a>
<span id="l281">    <span class="c"># Find &quot;the real&quot; strings.</span></span><a href="#l281"></a>
<span id="l282">    <span class="n">ws</span> <span class="o">=</span> <span class="n">want</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">ELLIPSIS_MARKER</span><span class="p">)</span></span><a href="#l282"></a>
<span id="l283">    <span class="k">assert</span> <span class="nb">len</span><span class="p">(</span><span class="n">ws</span><span class="p">)</span> <span class="o">&gt;=</span> <span class="mi">2</span></span><a href="#l283"></a>
<span id="l284"></span><a href="#l284"></a>
<span id="l285">    <span class="c"># Deal with exact matches possibly needed at one or both ends.</span></span><a href="#l285"></a>
<span id="l286">    <span class="n">startpos</span><span class="p">,</span> <span class="n">endpos</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">got</span><span class="p">)</span></span><a href="#l286"></a>
<span id="l287">    <span class="n">w</span> <span class="o">=</span> <span class="n">ws</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span></span><a href="#l287"></a>
<span id="l288">    <span class="k">if</span> <span class="n">w</span><span class="p">:</span>   <span class="c"># starts with exact match</span></span><a href="#l288"></a>
<span id="l289">        <span class="k">if</span> <span class="n">got</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="n">w</span><span class="p">):</span></span><a href="#l289"></a>
<span id="l290">            <span class="n">startpos</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">w</span><span class="p">)</span></span><a href="#l290"></a>
<span id="l291">            <span class="k">del</span> <span class="n">ws</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span></span><a href="#l291"></a>
<span id="l292">        <span class="k">else</span><span class="p">:</span></span><a href="#l292"></a>
<span id="l293">            <span class="k">return</span> <span class="bp">False</span></span><a href="#l293"></a>
<span id="l294">    <span class="n">w</span> <span class="o">=</span> <span class="n">ws</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span></span><a href="#l294"></a>
<span id="l295">    <span class="k">if</span> <span class="n">w</span><span class="p">:</span>   <span class="c"># ends with exact match</span></span><a href="#l295"></a>
<span id="l296">        <span class="k">if</span> <span class="n">got</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="n">w</span><span class="p">):</span></span><a href="#l296"></a>
<span id="l297">            <span class="n">endpos</span> <span class="o">-=</span> <span class="nb">len</span><span class="p">(</span><span class="n">w</span><span class="p">)</span></span><a href="#l297"></a>
<span id="l298">            <span class="k">del</span> <span class="n">ws</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span></span><a href="#l298"></a>
<span id="l299">        <span class="k">else</span><span class="p">:</span></span><a href="#l299"></a>
<span id="l300">            <span class="k">return</span> <span class="bp">False</span></span><a href="#l300"></a>
<span id="l301"></span><a href="#l301"></a>
<span id="l302">    <span class="k">if</span> <span class="n">startpos</span> <span class="o">&gt;</span> <span class="n">endpos</span><span class="p">:</span></span><a href="#l302"></a>
<span id="l303">        <span class="c"># Exact end matches required more characters than we have, as in</span></span><a href="#l303"></a>
<span id="l304">        <span class="c"># _ellipsis_match(&#39;aa...aa&#39;, &#39;aaa&#39;)</span></span><a href="#l304"></a>
<span id="l305">        <span class="k">return</span> <span class="bp">False</span></span><a href="#l305"></a>
<span id="l306"></span><a href="#l306"></a>
<span id="l307">    <span class="c"># For the rest, we only need to find the leftmost non-overlapping</span></span><a href="#l307"></a>
<span id="l308">    <span class="c"># match for each piece.  If there&#39;s no overall match that way alone,</span></span><a href="#l308"></a>
<span id="l309">    <span class="c"># there&#39;s no overall match period.</span></span><a href="#l309"></a>
<span id="l310">    <span class="k">for</span> <span class="n">w</span> <span class="ow">in</span> <span class="n">ws</span><span class="p">:</span></span><a href="#l310"></a>
<span id="l311">        <span class="c"># w may be &#39;&#39; at times, if there are consecutive ellipses, or</span></span><a href="#l311"></a>
<span id="l312">        <span class="c"># due to an ellipsis at the start or end of `want`.  That&#39;s OK.</span></span><a href="#l312"></a>
<span id="l313">        <span class="c"># Search for an empty string succeeds, and doesn&#39;t change startpos.</span></span><a href="#l313"></a>
<span id="l314">        <span class="n">startpos</span> <span class="o">=</span> <span class="n">got</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="n">w</span><span class="p">,</span> <span class="n">startpos</span><span class="p">,</span> <span class="n">endpos</span><span class="p">)</span></span><a href="#l314"></a>
<span id="l315">        <span class="k">if</span> <span class="n">startpos</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span></span><a href="#l315"></a>
<span id="l316">            <span class="k">return</span> <span class="bp">False</span></span><a href="#l316"></a>
<span id="l317">        <span class="n">startpos</span> <span class="o">+=</span> <span class="nb">len</span><span class="p">(</span><span class="n">w</span><span class="p">)</span></span><a href="#l317"></a>
<span id="l318"></span><a href="#l318"></a>
<span id="l319">    <span class="k">return</span> <span class="bp">True</span></span><a href="#l319"></a>
<span id="l320"></span><a href="#l320"></a>
<span id="l321"><span class="k">def</span> <span class="nf">_comment_line</span><span class="p">(</span><span class="n">line</span><span class="p">):</span></span><a href="#l321"></a>
<span id="l322">    <span class="s">&quot;Return a commented form of the given line&quot;</span></span><a href="#l322"></a>
<span id="l323">    <span class="n">line</span> <span class="o">=</span> <span class="n">line</span><span class="o">.</span><span class="n">rstrip</span><span class="p">()</span></span><a href="#l323"></a>
<span id="l324">    <span class="k">if</span> <span class="n">line</span><span class="p">:</span></span><a href="#l324"></a>
<span id="l325">        <span class="k">return</span> <span class="s">&#39;# &#39;</span><span class="o">+</span><span class="n">line</span></span><a href="#l325"></a>
<span id="l326">    <span class="k">else</span><span class="p">:</span></span><a href="#l326"></a>
<span id="l327">        <span class="k">return</span> <span class="s">&#39;#&#39;</span></span><a href="#l327"></a>
<span id="l328"></span><a href="#l328"></a>
<span id="l329"><span class="k">class</span> <span class="nc">_OutputRedirectingPdb</span><span class="p">(</span><span class="n">pdb</span><span class="o">.</span><span class="n">Pdb</span><span class="p">):</span></span><a href="#l329"></a>
<span id="l330">    <span class="sd">&quot;&quot;&quot;</span></span><a href="#l330"></a>
<span id="l331"><span class="sd">    A specialized version of the python debugger that redirects stdout</span></span><a href="#l331"></a>
<span id="l332"><span class="sd">    to a given stream when interacting with the user.  Stdout is *not*</span></span><a href="#l332"></a>
<span id="l333"><span class="sd">    redirected when traced code is executed.</span></span><a href="#l333"></a>
<span id="l334"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l334"></a>
<span id="l335">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">out</span><span class="p">):</span></span><a href="#l335"></a>
<span id="l336">        <span class="bp">self</span><span class="o">.</span><span class="n">__out</span> <span class="o">=</span> <span class="n">out</span></span><a href="#l336"></a>
<span id="l337">        <span class="bp">self</span><span class="o">.</span><span class="n">__debugger_used</span> <span class="o">=</span> <span class="bp">False</span></span><a href="#l337"></a>
<span id="l338">        <span class="n">pdb</span><span class="o">.</span><span class="n">Pdb</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">stdout</span><span class="o">=</span><span class="n">out</span><span class="p">)</span></span><a href="#l338"></a>
<span id="l339">        <span class="c"># still use input() to get user input</span></span><a href="#l339"></a>
<span id="l340">        <span class="bp">self</span><span class="o">.</span><span class="n">use_rawinput</span> <span class="o">=</span> <span class="mi">1</span></span><a href="#l340"></a>
<span id="l341"></span><a href="#l341"></a>
<span id="l342">    <span class="k">def</span> <span class="nf">set_trace</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">frame</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l342"></a>
<span id="l343">        <span class="bp">self</span><span class="o">.</span><span class="n">__debugger_used</span> <span class="o">=</span> <span class="bp">True</span></span><a href="#l343"></a>
<span id="l344">        <span class="k">if</span> <span class="n">frame</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l344"></a>
<span id="l345">            <span class="n">frame</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">_getframe</span><span class="p">()</span><span class="o">.</span><span class="n">f_back</span></span><a href="#l345"></a>
<span id="l346">        <span class="n">pdb</span><span class="o">.</span><span class="n">Pdb</span><span class="o">.</span><span class="n">set_trace</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">frame</span><span class="p">)</span></span><a href="#l346"></a>
<span id="l347"></span><a href="#l347"></a>
<span id="l348">    <span class="k">def</span> <span class="nf">set_continue</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l348"></a>
<span id="l349">        <span class="c"># Calling set_continue unconditionally would break unit test</span></span><a href="#l349"></a>
<span id="l350">        <span class="c"># coverage reporting, as Bdb.set_continue calls sys.settrace(None).</span></span><a href="#l350"></a>
<span id="l351">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">__debugger_used</span><span class="p">:</span></span><a href="#l351"></a>
<span id="l352">            <span class="n">pdb</span><span class="o">.</span><span class="n">Pdb</span><span class="o">.</span><span class="n">set_continue</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span></span><a href="#l352"></a>
<span id="l353"></span><a href="#l353"></a>
<span id="l354">    <span class="k">def</span> <span class="nf">trace_dispatch</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span></span><a href="#l354"></a>
<span id="l355">        <span class="c"># Redirect stdout to the given stream.</span></span><a href="#l355"></a>
<span id="l356">        <span class="n">save_stdout</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">stdout</span></span><a href="#l356"></a>
<span id="l357">        <span class="n">sys</span><span class="o">.</span><span class="n">stdout</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__out</span></span><a href="#l357"></a>
<span id="l358">        <span class="c"># Call Pdb&#39;s trace dispatch method.</span></span><a href="#l358"></a>
<span id="l359">        <span class="k">try</span><span class="p">:</span></span><a href="#l359"></a>
<span id="l360">            <span class="k">return</span> <span class="n">pdb</span><span class="o">.</span><span class="n">Pdb</span><span class="o">.</span><span class="n">trace_dispatch</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span></span><a href="#l360"></a>
<span id="l361">        <span class="k">finally</span><span class="p">:</span></span><a href="#l361"></a>
<span id="l362">            <span class="n">sys</span><span class="o">.</span><span class="n">stdout</span> <span class="o">=</span> <span class="n">save_stdout</span></span><a href="#l362"></a>
<span id="l363"></span><a href="#l363"></a>
<span id="l364"><span class="c"># [XX] Normalize with respect to os.path.pardir?</span></span><a href="#l364"></a>
<span id="l365"><span class="k">def</span> <span class="nf">_module_relative_path</span><span class="p">(</span><span class="n">module</span><span class="p">,</span> <span class="n">path</span><span class="p">):</span></span><a href="#l365"></a>
<span id="l366">    <span class="k">if</span> <span class="ow">not</span> <span class="n">inspect</span><span class="o">.</span><span class="n">ismodule</span><span class="p">(</span><span class="n">module</span><span class="p">):</span></span><a href="#l366"></a>
<span id="l367">        <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">,</span> <span class="s">&#39;Expected a module: </span><span class="si">%r</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">module</span></span><a href="#l367"></a>
<span id="l368">    <span class="k">if</span> <span class="n">path</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s">&#39;/&#39;</span><span class="p">):</span></span><a href="#l368"></a>
<span id="l369">        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">,</span> <span class="s">&#39;Module-relative files may not have absolute paths&#39;</span></span><a href="#l369"></a>
<span id="l370"></span><a href="#l370"></a>
<span id="l371">    <span class="c"># Find the base directory for the path.</span></span><a href="#l371"></a>
<span id="l372">    <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">module</span><span class="p">,</span> <span class="s">&#39;__file__&#39;</span><span class="p">):</span></span><a href="#l372"></a>
<span id="l373">        <span class="c"># A normal module/package</span></span><a href="#l373"></a>
<span id="l374">        <span class="n">basedir</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">module</span><span class="o">.</span><span class="n">__file__</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span></span><a href="#l374"></a>
<span id="l375">    <span class="k">elif</span> <span class="n">module</span><span class="o">.</span><span class="n">__name__</span> <span class="o">==</span> <span class="s">&#39;__main__&#39;</span><span class="p">:</span></span><a href="#l375"></a>
<span id="l376">        <span class="c"># An interactive session.</span></span><a href="#l376"></a>
<span id="l377">        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">)</span><span class="o">&gt;</span><span class="mi">0</span> <span class="ow">and</span> <span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">!=</span> <span class="s">&#39;&#39;</span><span class="p">:</span></span><a href="#l377"></a>
<span id="l378">            <span class="n">basedir</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">0</span><span class="p">])[</span><span class="mi">0</span><span class="p">]</span></span><a href="#l378"></a>
<span id="l379">        <span class="k">else</span><span class="p">:</span></span><a href="#l379"></a>
<span id="l380">            <span class="n">basedir</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">curdir</span></span><a href="#l380"></a>
<span id="l381">    <span class="k">else</span><span class="p">:</span></span><a href="#l381"></a>
<span id="l382">        <span class="c"># A module w/o __file__ (this includes builtins)</span></span><a href="#l382"></a>
<span id="l383">        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&quot;Can&#39;t resolve paths relative to the module &quot;</span> <span class="o">+</span></span><a href="#l383"></a>
<span id="l384">                         <span class="n">module</span> <span class="o">+</span> <span class="s">&quot; (it has no __file__)&quot;</span><span class="p">)</span></span><a href="#l384"></a>
<span id="l385"></span><a href="#l385"></a>
<span id="l386">    <span class="c"># Combine the base directory and the path.</span></span><a href="#l386"></a>
<span id="l387">    <span class="k">return</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">basedir</span><span class="p">,</span> <span class="o">*</span><span class="p">(</span><span class="n">path</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;/&#39;</span><span class="p">)))</span></span><a href="#l387"></a>
<span id="l388"></span><a href="#l388"></a>
<span id="l389"><span class="c">######################################################################</span></span><a href="#l389"></a>
<span id="l390"><span class="c">## 2. Example &amp; DocTest</span></span><a href="#l390"></a>
<span id="l391"><span class="c">######################################################################</span></span><a href="#l391"></a>
<span id="l392"><span class="c">## - An &quot;example&quot; is a &lt;source, want&gt; pair, where &quot;source&quot; is a</span></span><a href="#l392"></a>
<span id="l393"><span class="c">##   fragment of source code, and &quot;want&quot; is the expected output for</span></span><a href="#l393"></a>
<span id="l394"><span class="c">##   &quot;source.&quot;  The Example class also includes information about</span></span><a href="#l394"></a>
<span id="l395"><span class="c">##   where the example was extracted from.</span></span><a href="#l395"></a>
<span id="l396"><span class="c">##</span></span><a href="#l396"></a>
<span id="l397"><span class="c">## - A &quot;doctest&quot; is a collection of examples, typically extracted from</span></span><a href="#l397"></a>
<span id="l398"><span class="c">##   a string (such as an object&#39;s docstring).  The DocTest class also</span></span><a href="#l398"></a>
<span id="l399"><span class="c">##   includes information about where the string was extracted from.</span></span><a href="#l399"></a>
<span id="l400"></span><a href="#l400"></a>
<span id="l401"><span class="k">class</span> <span class="nc">Example</span><span class="p">:</span></span><a href="#l401"></a>
<span id="l402">    <span class="sd">&quot;&quot;&quot;</span></span><a href="#l402"></a>
<span id="l403"><span class="sd">    A single doctest example, consisting of source code and expected</span></span><a href="#l403"></a>
<span id="l404"><span class="sd">    output.  `Example` defines the following attributes:</span></span><a href="#l404"></a>
<span id="l405"></span><a href="#l405"></a>
<span id="l406"><span class="sd">      - source: A single Python statement, always ending with a newline.</span></span><a href="#l406"></a>
<span id="l407"><span class="sd">        The constructor adds a newline if needed.</span></span><a href="#l407"></a>
<span id="l408"></span><a href="#l408"></a>
<span id="l409"><span class="sd">      - want: The expected output from running the source code (either</span></span><a href="#l409"></a>
<span id="l410"><span class="sd">        from stdout, or a traceback in case of exception).  `want` ends</span></span><a href="#l410"></a>
<span id="l411"><span class="sd">        with a newline unless it&#39;s empty, in which case it&#39;s an empty</span></span><a href="#l411"></a>
<span id="l412"><span class="sd">        string.  The constructor adds a newline if needed.</span></span><a href="#l412"></a>
<span id="l413"></span><a href="#l413"></a>
<span id="l414"><span class="sd">      - exc_msg: The exception message generated by the example, if</span></span><a href="#l414"></a>
<span id="l415"><span class="sd">        the example is expected to generate an exception; or `None` if</span></span><a href="#l415"></a>
<span id="l416"><span class="sd">        it is not expected to generate an exception.  This exception</span></span><a href="#l416"></a>
<span id="l417"><span class="sd">        message is compared against the return value of</span></span><a href="#l417"></a>
<span id="l418"><span class="sd">        `traceback.format_exception_only()`.  `exc_msg` ends with a</span></span><a href="#l418"></a>
<span id="l419"><span class="sd">        newline unless it&#39;s `None`.  The constructor adds a newline</span></span><a href="#l419"></a>
<span id="l420"><span class="sd">        if needed.</span></span><a href="#l420"></a>
<span id="l421"></span><a href="#l421"></a>
<span id="l422"><span class="sd">      - lineno: The line number within the DocTest string containing</span></span><a href="#l422"></a>
<span id="l423"><span class="sd">        this Example where the Example begins.  This line number is</span></span><a href="#l423"></a>
<span id="l424"><span class="sd">        zero-based, with respect to the beginning of the DocTest.</span></span><a href="#l424"></a>
<span id="l425"></span><a href="#l425"></a>
<span id="l426"><span class="sd">      - indent: The example&#39;s indentation in the DocTest string.</span></span><a href="#l426"></a>
<span id="l427"><span class="sd">        I.e., the number of space characters that preceed the</span></span><a href="#l427"></a>
<span id="l428"><span class="sd">        example&#39;s first prompt.</span></span><a href="#l428"></a>
<span id="l429"></span><a href="#l429"></a>
<span id="l430"><span class="sd">      - options: A dictionary mapping from option flags to True or</span></span><a href="#l430"></a>
<span id="l431"><span class="sd">        False, which is used to override default options for this</span></span><a href="#l431"></a>
<span id="l432"><span class="sd">        example.  Any option flags not contained in this dictionary</span></span><a href="#l432"></a>
<span id="l433"><span class="sd">        are left at their default value (as specified by the</span></span><a href="#l433"></a>
<span id="l434"><span class="sd">        DocTestRunner&#39;s optionflags).  By default, no options are set.</span></span><a href="#l434"></a>
<span id="l435"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l435"></a>
<span id="l436">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">source</span><span class="p">,</span> <span class="n">want</span><span class="p">,</span> <span class="n">exc_msg</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">lineno</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">indent</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span></span><a href="#l436"></a>
<span id="l437">                 <span class="n">options</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l437"></a>
<span id="l438">        <span class="c"># Normalize inputs.</span></span><a href="#l438"></a>
<span id="l439">        <span class="k">if</span> <span class="ow">not</span> <span class="n">source</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">):</span></span><a href="#l439"></a>
<span id="l440">            <span class="n">source</span> <span class="o">+=</span> <span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span></span><a href="#l440"></a>
<span id="l441">        <span class="k">if</span> <span class="n">want</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">want</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">):</span></span><a href="#l441"></a>
<span id="l442">            <span class="n">want</span> <span class="o">+=</span> <span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span></span><a href="#l442"></a>
<span id="l443">        <span class="k">if</span> <span class="n">exc_msg</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">exc_msg</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">):</span></span><a href="#l443"></a>
<span id="l444">            <span class="n">exc_msg</span> <span class="o">+=</span> <span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span></span><a href="#l444"></a>
<span id="l445">        <span class="c"># Store properties.</span></span><a href="#l445"></a>
<span id="l446">        <span class="bp">self</span><span class="o">.</span><span class="n">source</span> <span class="o">=</span> <span class="n">source</span></span><a href="#l446"></a>
<span id="l447">        <span class="bp">self</span><span class="o">.</span><span class="n">want</span> <span class="o">=</span> <span class="n">want</span></span><a href="#l447"></a>
<span id="l448">        <span class="bp">self</span><span class="o">.</span><span class="n">lineno</span> <span class="o">=</span> <span class="n">lineno</span></span><a href="#l448"></a>
<span id="l449">        <span class="bp">self</span><span class="o">.</span><span class="n">indent</span> <span class="o">=</span> <span class="n">indent</span></span><a href="#l449"></a>
<span id="l450">        <span class="k">if</span> <span class="n">options</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span> <span class="n">options</span> <span class="o">=</span> <span class="p">{}</span></span><a href="#l450"></a>
<span id="l451">        <span class="bp">self</span><span class="o">.</span><span class="n">options</span> <span class="o">=</span> <span class="n">options</span></span><a href="#l451"></a>
<span id="l452">        <span class="bp">self</span><span class="o">.</span><span class="n">exc_msg</span> <span class="o">=</span> <span class="n">exc_msg</span></span><a href="#l452"></a>
<span id="l453"></span><a href="#l453"></a>
<span id="l454">    <span class="k">def</span> <span class="nf">__eq__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l454"></a>
<span id="l455">        <span class="k">if</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="ow">is</span> <span class="ow">not</span> <span class="nb">type</span><span class="p">(</span><span class="n">other</span><span class="p">):</span></span><a href="#l455"></a>
<span id="l456">            <span class="k">return</span> <span class="bp">NotImplemented</span></span><a href="#l456"></a>
<span id="l457"></span><a href="#l457"></a>
<span id="l458">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">source</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">source</span> <span class="ow">and</span> \</span><a href="#l458"></a>
<span id="l459">               <span class="bp">self</span><span class="o">.</span><span class="n">want</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">want</span> <span class="ow">and</span> \</span><a href="#l459"></a>
<span id="l460">               <span class="bp">self</span><span class="o">.</span><span class="n">lineno</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">lineno</span> <span class="ow">and</span> \</span><a href="#l460"></a>
<span id="l461">               <span class="bp">self</span><span class="o">.</span><span class="n">indent</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">indent</span> <span class="ow">and</span> \</span><a href="#l461"></a>
<span id="l462">               <span class="bp">self</span><span class="o">.</span><span class="n">options</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">options</span> <span class="ow">and</span> \</span><a href="#l462"></a>
<span id="l463">               <span class="bp">self</span><span class="o">.</span><span class="n">exc_msg</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">exc_msg</span></span><a href="#l463"></a>
<span id="l464"></span><a href="#l464"></a>
<span id="l465">    <span class="k">def</span> <span class="nf">__ne__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l465"></a>
<span id="l466">        <span class="k">return</span> <span class="ow">not</span> <span class="bp">self</span> <span class="o">==</span> <span class="n">other</span></span><a href="#l466"></a>
<span id="l467"></span><a href="#l467"></a>
<span id="l468">    <span class="k">def</span> <span class="nf">__hash__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l468"></a>
<span id="l469">        <span class="k">return</span> <span class="nb">hash</span><span class="p">((</span><span class="bp">self</span><span class="o">.</span><span class="n">source</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">want</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">lineno</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">indent</span><span class="p">,</span></span><a href="#l469"></a>
<span id="l470">                     <span class="bp">self</span><span class="o">.</span><span class="n">exc_msg</span><span class="p">))</span></span><a href="#l470"></a>
<span id="l471"></span><a href="#l471"></a>
<span id="l472"></span><a href="#l472"></a>
<span id="l473"><span class="k">class</span> <span class="nc">DocTest</span><span class="p">:</span></span><a href="#l473"></a>
<span id="l474">    <span class="sd">&quot;&quot;&quot;</span></span><a href="#l474"></a>
<span id="l475"><span class="sd">    A collection of doctest examples that should be run in a single</span></span><a href="#l475"></a>
<span id="l476"><span class="sd">    namespace.  Each `DocTest` defines the following attributes:</span></span><a href="#l476"></a>
<span id="l477"></span><a href="#l477"></a>
<span id="l478"><span class="sd">      - examples: the list of examples.</span></span><a href="#l478"></a>
<span id="l479"></span><a href="#l479"></a>
<span id="l480"><span class="sd">      - globs: The namespace (aka globals) that the examples should</span></span><a href="#l480"></a>
<span id="l481"><span class="sd">        be run in.</span></span><a href="#l481"></a>
<span id="l482"></span><a href="#l482"></a>
<span id="l483"><span class="sd">      - name: A name identifying the DocTest (typically, the name of</span></span><a href="#l483"></a>
<span id="l484"><span class="sd">        the object whose docstring this DocTest was extracted from).</span></span><a href="#l484"></a>
<span id="l485"></span><a href="#l485"></a>
<span id="l486"><span class="sd">      - filename: The name of the file that this DocTest was extracted</span></span><a href="#l486"></a>
<span id="l487"><span class="sd">        from, or `None` if the filename is unknown.</span></span><a href="#l487"></a>
<span id="l488"></span><a href="#l488"></a>
<span id="l489"><span class="sd">      - lineno: The line number within filename where this DocTest</span></span><a href="#l489"></a>
<span id="l490"><span class="sd">        begins, or `None` if the line number is unavailable.  This</span></span><a href="#l490"></a>
<span id="l491"><span class="sd">        line number is zero-based, with respect to the beginning of</span></span><a href="#l491"></a>
<span id="l492"><span class="sd">        the file.</span></span><a href="#l492"></a>
<span id="l493"></span><a href="#l493"></a>
<span id="l494"><span class="sd">      - docstring: The string that the examples were extracted from,</span></span><a href="#l494"></a>
<span id="l495"><span class="sd">        or `None` if the string is unavailable.</span></span><a href="#l495"></a>
<span id="l496"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l496"></a>
<span id="l497">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">examples</span><span class="p">,</span> <span class="n">globs</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">filename</span><span class="p">,</span> <span class="n">lineno</span><span class="p">,</span> <span class="n">docstring</span><span class="p">):</span></span><a href="#l497"></a>
<span id="l498">        <span class="sd">&quot;&quot;&quot;</span></span><a href="#l498"></a>
<span id="l499"><span class="sd">        Create a new DocTest containing the given examples.  The</span></span><a href="#l499"></a>
<span id="l500"><span class="sd">        DocTest&#39;s globals are initialized with a copy of `globs`.</span></span><a href="#l500"></a>
<span id="l501"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l501"></a>
<span id="l502">        <span class="k">assert</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">examples</span><span class="p">,</span> <span class="nb">basestring</span><span class="p">),</span> \</span><a href="#l502"></a>
<span id="l503">               <span class="s">&quot;DocTest no longer accepts str; use DocTestParser instead&quot;</span></span><a href="#l503"></a>
<span id="l504">        <span class="bp">self</span><span class="o">.</span><span class="n">examples</span> <span class="o">=</span> <span class="n">examples</span></span><a href="#l504"></a>
<span id="l505">        <span class="bp">self</span><span class="o">.</span><span class="n">docstring</span> <span class="o">=</span> <span class="n">docstring</span></span><a href="#l505"></a>
<span id="l506">        <span class="bp">self</span><span class="o">.</span><span class="n">globs</span> <span class="o">=</span> <span class="n">globs</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span></span><a href="#l506"></a>
<span id="l507">        <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="o">=</span> <span class="n">name</span></span><a href="#l507"></a>
<span id="l508">        <span class="bp">self</span><span class="o">.</span><span class="n">filename</span> <span class="o">=</span> <span class="n">filename</span></span><a href="#l508"></a>
<span id="l509">        <span class="bp">self</span><span class="o">.</span><span class="n">lineno</span> <span class="o">=</span> <span class="n">lineno</span></span><a href="#l509"></a>
<span id="l510"></span><a href="#l510"></a>
<span id="l511">    <span class="k">def</span> <span class="nf">__repr__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l511"></a>
<span id="l512">        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span></span><a href="#l512"></a>
<span id="l513">            <span class="n">examples</span> <span class="o">=</span> <span class="s">&#39;no examples&#39;</span></span><a href="#l513"></a>
<span id="l514">        <span class="k">elif</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">)</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span></span><a href="#l514"></a>
<span id="l515">            <span class="n">examples</span> <span class="o">=</span> <span class="s">&#39;1 example&#39;</span></span><a href="#l515"></a>
<span id="l516">        <span class="k">else</span><span class="p">:</span></span><a href="#l516"></a>
<span id="l517">            <span class="n">examples</span> <span class="o">=</span> <span class="s">&#39;</span><span class="si">%d</span><span class="s"> examples&#39;</span> <span class="o">%</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">examples</span><span class="p">)</span></span><a href="#l517"></a>
<span id="l518">        <span class="k">return</span> <span class="p">(</span><span class="s">&#39;&lt;DocTest </span><span class="si">%s</span><span class="s"> from </span><span class="si">%s</span><span class="s">:</span><span class="si">%s</span><span class="s"> (</span><span class="si">%s</span><span class="s">)&gt;&#39;</span> <span class="o">%</span></span><a href="#l518"></a>
<span id="l519">                <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">filename</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">lineno</span><span class="p">,</span> <span class="n">examples</span><span class="p">))</span></span><a href="#l519"></a>
<span id="l520"></span><a href="#l520"></a>
<span id="l521">    <span class="k">def</span> <span class="nf">__eq__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l521"></a>
<span id="l522">        <span class="k">if</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="ow">is</span> <span class="ow">not</span> <span class="nb">type</span><span class="p">(</span><span class="n">other</span><span class="p">):</span></span><a href="#l522"></a>
<span id="l523">            <span class="k">return</span> <span class="bp">NotImplemented</span></span><a href="#l523"></a>
<span id="l524"></span><a href="#l524"></a>
<span id="l525">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">examples</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">examples</span> <span class="ow">and</span> \</span><a href="#l525"></a>
<span id="l526">               <span class="bp">self</span><span class="o">.</span><span class="n">docstring</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">docstring</span> <span class="ow">and</span> \</span><a href="#l526"></a>
<span id="l527">               <span class="bp">self</span><span class="o">.</span><span class="n">globs</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">globs</span> <span class="ow">and</span> \</span><a href="#l527"></a>
<span id="l528">               <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">name</span> <span class="ow">and</span> \</span><a href="#l528"></a>
<span id="l529">               <span class="bp">self</span><span class="o">.</span><span class="n">filename</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">filename</span> <span class="ow">and</span> \</span><a href="#l529"></a>
<span id="l530">               <span class="bp">self</span><span class="o">.</span><span class="n">lineno</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">lineno</span></span><a href="#l530"></a>
<span id="l531"></span><a href="#l531"></a>
<span id="l532">    <span class="k">def</span> <span class="nf">__ne__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l532"></a>
<span id="l533">        <span class="k">return</span> <span class="ow">not</span> <span class="bp">self</span> <span class="o">==</span> <span class="n">other</span></span><a href="#l533"></a>
<span id="l534"></span><a href="#l534"></a>
<span id="l535">    <span class="k">def</span> <span class="nf">__hash__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l535"></a>
<span id="l536">        <span class="k">return</span> <span class="nb">hash</span><span class="p">((</span><span class="bp">self</span><span class="o">.</span><span class="n">docstring</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">filename</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">lineno</span><span class="p">))</span></span><a href="#l536"></a>
<span id="l537"></span><a href="#l537"></a>
<span id="l538">    <span class="c"># This lets us sort tests by name:</span></span><a href="#l538"></a>
<span id="l539">    <span class="k">def</span> <span class="nf">__cmp__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l539"></a>
<span id="l540">        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">DocTest</span><span class="p">):</span></span><a href="#l540"></a>
<span id="l541">            <span class="k">return</span> <span class="o">-</span><span class="mi">1</span></span><a href="#l541"></a>
<span id="l542">        <span class="k">return</span> <span class="nb">cmp</span><span class="p">((</span><span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">filename</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">lineno</span><span class="p">,</span> <span class="nb">id</span><span class="p">(</span><span class="bp">self</span><span class="p">)),</span></span><a href="#l542"></a>
<span id="l543">                   <span class="p">(</span><span class="n">other</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="n">other</span><span class="o">.</span><span class="n">filename</span><span class="p">,</span> <span class="n">other</span><span class="o">.</span><span class="n">lineno</span><span class="p">,</span> <span class="nb">id</span><span class="p">(</span><span class="n">other</span><span class="p">)))</span></span><a href="#l543"></a>
<span id="l544"></span><a href="#l544"></a>
<span id="l545"><span class="c">######################################################################</span></span><a href="#l545"></a>
<span id="l546"><span class="c">## 3. DocTestParser</span></span><a href="#l546"></a>
<span id="l547"><span class="c">######################################################################</span></span><a href="#l547"></a>
<span id="l548"></span><a href="#l548"></a>
<span id="l549"><span class="k">class</span> <span class="nc">DocTestParser</span><span class="p">:</span></span><a href="#l549"></a>
<span id="l550">    <span class="sd">&quot;&quot;&quot;</span></span><a href="#l550"></a>
<span id="l551"><span class="sd">    A class used to parse strings containing doctest examples.</span></span><a href="#l551"></a>
<span id="l552"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l552"></a>
<span id="l553">    <span class="c"># This regular expression is used to find doctest examples in a</span></span><a href="#l553"></a>
<span id="l554">    <span class="c"># string.  It defines three groups: `source` is the source code</span></span><a href="#l554"></a>
<span id="l555">    <span class="c"># (including leading indentation and prompts); `indent` is the</span></span><a href="#l555"></a>
<span id="l556">    <span class="c"># indentation of the first (PS1) line of the source code; and</span></span><a href="#l556"></a>
<span id="l557">    <span class="c"># `want` is the expected output (including leading indentation).</span></span><a href="#l557"></a>
<span id="l558">    <span class="n">_EXAMPLE_RE</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="s">r&#39;&#39;&#39;</span></span><a href="#l558"></a>
<span id="l559"><span class="s">        # Source consists of a PS1 line followed by zero or more PS2 lines.</span></span><a href="#l559"></a>
<span id="l560"><span class="s">        (?P&lt;source&gt;</span></span><a href="#l560"></a>
<span id="l561"><span class="s">            (?:^(?P&lt;indent&gt; [ ]*) &gt;&gt;&gt;    .*)    # PS1 line</span></span><a href="#l561"></a>
<span id="l562"><span class="s">            (?:\n           [ ]*  \.\.\. .*)*)  # PS2 lines</span></span><a href="#l562"></a>
<span id="l563"><span class="s">        \n?</span></span><a href="#l563"></a>
<span id="l564"><span class="s">        # Want consists of any non-blank lines that do not start with PS1.</span></span><a href="#l564"></a>
<span id="l565"><span class="s">        (?P&lt;want&gt; (?:(?![ ]*$)    # Not a blank line</span></span><a href="#l565"></a>
<span id="l566"><span class="s">                     (?![ ]*&gt;&gt;&gt;)  # Not a line starting with PS1</span></span><a href="#l566"></a>
<span id="l567"><span class="s">                     .*$\n?       # But any other line</span></span><a href="#l567"></a>
<span id="l568"><span class="s">                  )*)</span></span><a href="#l568"></a>
<span id="l569"><span class="s">        &#39;&#39;&#39;</span><span class="p">,</span> <span class="n">re</span><span class="o">.</span><span class="n">MULTILINE</span> <span class="o">|</span> <span class="n">re</span><span class="o">.</span><span class="n">VERBOSE</span><span class="p">)</span></span><a href="#l569"></a>
<span id="l570"></span><a href="#l570"></a>
<span id="l571">    <span class="c"># A regular expression for handling `want` strings that contain</span></span><a href="#l571"></a>
<span id="l572">    <span class="c"># expected exceptions.  It divides `want` into three pieces:</span></span><a href="#l572"></a>
<span id="l573">    <span class="c">#    - the traceback header line (`hdr`)</span></span><a href="#l573"></a>
<span id="l574">    <span class="c">#    - the traceback stack (`stack`)</span></span><a href="#l574"></a>
<span id="l575">    <span class="c">#    - the exception message (`msg`), as generated by</span></span><a href="#l575"></a>
<span id="l576">    <span class="c">#      traceback.format_exception_only()</span></span><a href="#l576"></a>
<span id="l577">    <span class="c"># `msg` may have multiple lines.  We assume/require that the</span></span><a href="#l577"></a>
<span id="l578">    <span class="c"># exception message is the first non-indented line starting with a word</span></span><a href="#l578"></a>
<span id="l579">    <span class="c"># character following the traceback header line.</span></span><a href="#l579"></a>
<span id="l580">    <span class="n">_EXCEPTION_RE</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="s">r&quot;&quot;&quot;</span></span><a href="#l580"></a>
<span id="l581"><span class="s">        # Grab the traceback header.  Different versions of Python have</span></span><a href="#l581"></a>
<span id="l582"><span class="s">        # said different things on the first traceback line.</span></span><a href="#l582"></a>
<span id="l583"><span class="s">        ^(?P&lt;hdr&gt; Traceback\ \(</span></span><a href="#l583"></a>
<span id="l584"><span class="s">            (?: most\ recent\ call\ last</span></span><a href="#l584"></a>
<span id="l585"><span class="s">            |   innermost\ last</span></span><a href="#l585"></a>
<span id="l586"><span class="s">            ) \) :</span></span><a href="#l586"></a>
<span id="l587"><span class="s">        )</span></span><a href="#l587"></a>
<span id="l588"><span class="s">        \s* $                # toss trailing whitespace on the header.</span></span><a href="#l588"></a>
<span id="l589"><span class="s">        (?P&lt;stack&gt; .*?)      # don&#39;t blink: absorb stuff until...</span></span><a href="#l589"></a>
<span id="l590"><span class="s">        ^ (?P&lt;msg&gt; \w+ .*)   #     a line *starts* with alphanum.</span></span><a href="#l590"></a>
<span id="l591"><span class="s">        &quot;&quot;&quot;</span><span class="p">,</span> <span class="n">re</span><span class="o">.</span><span class="n">VERBOSE</span> <span class="o">|</span> <span class="n">re</span><span class="o">.</span><span class="n">MULTILINE</span> <span class="o">|</span> <span class="n">re</span><span class="o">.</span><span class="n">DOTALL</span><span class="p">)</span></span><a href="#l591"></a>
<span id="l592"></span><a href="#l592"></a>
<span id="l593">    <span class="c"># A callable returning a true value iff its argument is a blank line</span></span><a href="#l593"></a>
<span id="l594">    <span class="c"># or contains a single comment.</span></span><a href="#l594"></a>
<span id="l595">    <span class="n">_IS_BLANK_OR_COMMENT</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="s">r&#39;^[ ]*(#.*)?$&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">match</span></span><a href="#l595"></a>
<span id="l596"></span><a href="#l596"></a>
<span id="l597">    <span class="k">def</span> <span class="nf">parse</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">string</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s">&#39;&lt;string&gt;&#39;</span><span class="p">):</span></span><a href="#l597"></a>
<span id="l598">        <span class="sd">&quot;&quot;&quot;</span></span><a href="#l598"></a>
<span id="l599"><span class="sd">        Divide the given string into examples and intervening text,</span></span><a href="#l599"></a>
<span id="l600"><span class="sd">        and return them as a list of alternating Examples and strings.</span></span><a href="#l600"></a>
<span id="l601"><span class="sd">        Line numbers for the Examples are 0-based.  The optional</span></span><a href="#l601"></a>
<span id="l602"><span class="sd">        argument `name` is a name identifying this string, and is only</span></span><a href="#l602"></a>
<span id="l603"><span class="sd">        used for error messages.</span></span><a href="#l603"></a>
<span id="l604"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l604"></a>
<span id="l605">        <span class="n">string</span> <span class="o">=</span> <span class="n">string</span><span class="o">.</span><span class="n">expandtabs</span><span class="p">()</span></span><a href="#l605"></a>
<span id="l606">        <span class="c"># If all lines begin with the same indentation, then strip it.</span></span><a href="#l606"></a>
<span id="l607">        <span class="n">min_indent</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_min_indent</span><span class="p">(</span><span class="n">string</span><span class="p">)</span></span><a href="#l607"></a>
<span id="l608">        <span class="k">if</span> <span class="n">min_indent</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span></span><a href="#l608"></a>
<span id="l609">            <span class="n">string</span> <span class="o">=</span> <span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">l</span><span class="p">[</span><span class="n">min_indent</span><span class="p">:]</span> <span class="k">for</span> <span class="n">l</span> <span class="ow">in</span> <span class="n">string</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)])</span></span><a href="#l609"></a>
<span id="l610"></span><a href="#l610"></a>
<span id="l611">        <span class="n">output</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l611"></a>
<span id="l612">        <span class="n">charno</span><span class="p">,</span> <span class="n">lineno</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span></span><a href="#l612"></a>
<span id="l613">        <span class="c"># Find all doctest examples in the string:</span></span><a href="#l613"></a>
<span id="l614">        <span class="k">for</span> <span class="n">m</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_EXAMPLE_RE</span><span class="o">.</span><span class="n">finditer</span><span class="p">(</span><span class="n">string</span><span class="p">):</span></span><a href="#l614"></a>
<span id="l615">            <span class="c"># Add the pre-example text to `output`.</span></span><a href="#l615"></a>
<span id="l616">            <span class="n">output</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">string</span><span class="p">[</span><span class="n">charno</span><span class="p">:</span><span class="n">m</span><span class="o">.</span><span class="n">start</span><span class="p">()])</span></span><a href="#l616"></a>
<span id="l617">            <span class="c"># Update lineno (lines before this example)</span></span><a href="#l617"></a>
<span id="l618">            <span class="n">lineno</span> <span class="o">+=</span> <span class="n">string</span><span class="o">.</span><span class="n">count</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">,</span> <span class="n">charno</span><span class="p">,</span> <span class="n">m</span><span class="o">.</span><span class="n">start</span><span class="p">())</span></span><a href="#l618"></a>
<span id="l619">            <span class="c"># Extract info from the regexp match.</span></span><a href="#l619"></a>
<span id="l620">            <span class="p">(</span><span class="n">source</span><span class="p">,</span> <span class="n">options</span><span class="p">,</span> <span class="n">want</span><span class="p">,</span> <span class="n">exc_msg</span><span class="p">)</span> <span class="o">=</span> \</span><a href="#l620"></a>
<span id="l621">                     <span class="bp">self</span><span class="o">.</span><span class="n">_parse_example</span><span class="p">(</span><span class="n">m</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">lineno</span><span class="p">)</span></span><a href="#l621"></a>
<span id="l622">            <span class="c"># Create an Example, and add it to the list.</span></span><a href="#l622"></a>
<span id="l623">            <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_IS_BLANK_OR_COMMENT</span><span class="p">(</span><span class="n">source</span><span class="p">):</span></span><a href="#l623"></a>
<span id="l624">                <span class="n">output</span><span class="o">.</span><span class="n">append</span><span class="p">(</span> <span class="n">Example</span><span class="p">(</span><span class="n">source</span><span class="p">,</span> <span class="n">want</span><span class="p">,</span> <span class="n">exc_msg</span><span class="p">,</span></span><a href="#l624"></a>
<span id="l625">                                    <span class="n">lineno</span><span class="o">=</span><span class="n">lineno</span><span class="p">,</span></span><a href="#l625"></a>
<span id="l626">                                    <span class="n">indent</span><span class="o">=</span><span class="n">min_indent</span><span class="o">+</span><span class="nb">len</span><span class="p">(</span><span class="n">m</span><span class="o">.</span><span class="n">group</span><span class="p">(</span><span class="s">&#39;indent&#39;</span><span class="p">)),</span></span><a href="#l626"></a>
<span id="l627">                                    <span class="n">options</span><span class="o">=</span><span class="n">options</span><span class="p">)</span> <span class="p">)</span></span><a href="#l627"></a>
<span id="l628">            <span class="c"># Update lineno (lines inside this example)</span></span><a href="#l628"></a>
<span id="l629">            <span class="n">lineno</span> <span class="o">+=</span> <span class="n">string</span><span class="o">.</span><span class="n">count</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">,</span> <span class="n">m</span><span class="o">.</span><span class="n">start</span><span class="p">(),</span> <span class="n">m</span><span class="o">.</span><span class="n">end</span><span class="p">())</span></span><a href="#l629"></a>
<span id="l630">            <span class="c"># Update charno.</span></span><a href="#l630"></a>
<span id="l631">            <span class="n">charno</span> <span class="o">=</span> <span class="n">m</span><span class="o">.</span><span class="n">end</span><span class="p">()</span></span><a href="#l631"></a>
<span id="l632">        <span class="c"># Add any remaining post-example text to `output`.</span></span><a href="#l632"></a>
<span id="l633">        <span class="n">output</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">string</span><span class="p">[</span><span class="n">charno</span><span class="p">:])</span></span><a href="#l633"></a>
<span id="l634">        <span class="k">return</span> <span class="n">output</span></span><a href="#l634"></a>
<span id="l635"></span><a href="#l635"></a>
<span id="l636">    <span class="k">def</span> <span class="nf">get_doctest</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">string</span><span class="p">,</span> <span class="n">globs</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">filename</span><span class="p">,</span> <span class="n">lineno</span><span class="p">):</span></span><a href="#l636"></a>
<span id="l637">        <span class="sd">&quot;&quot;&quot;</span></span><a href="#l637"></a>
<span id="l638"><span class="sd">        Extract all doctest examples from the given string, and</span></span><a href="#l638"></a>
<span id="l639"><span class="sd">        collect them into a `DocTest` object.</span></span><a href="#l639"></a>
<span id="l640"></span><a href="#l640"></a>
<span id="l641"><span class="sd">        `globs`, `name`, `filename`, and `lineno` are attributes for</span></span><a href="#l641"></a>
<span id="l642"><span class="sd">        the new `DocTest` object.  See the documentation for `DocTest`</span></span><a href="#l642"></a>
<span id="l643"><span class="sd">        for more information.</span></span><a href="#l643"></a>
<span id="l644"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l644"></a>
<span id="l645">        <span class="k">return</span> <span class="n">DocTest</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_examples</span><span class="p">(</span><span class="n">string</span><span class="p">,</span> <span class="n">name</span><span class="p">),</span> <span class="n">globs</span><span class="p">,</span></span><a href="#l645"></a>
<span id="l646">                       <span class="n">name</span><span class="p">,</span> <span class="n">filename</span><span class="p">,</span> <span class="n">lineno</span><span class="p">,</span> <span class="n">string</span><span class="p">)</span></span><a href="#l646"></a>
<span id="l647"></span><a href="#l647"></a>
<span id="l648">    <span class="k">def</span> <span class="nf">get_examples</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">string</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s">&#39;&lt;string&gt;&#39;</span><span class="p">):</span></span><a href="#l648"></a>
<span id="l649">        <span class="sd">&quot;&quot;&quot;</span></span><a href="#l649"></a>
<span id="l650"><span class="sd">        Extract all doctest examples from the given string, and return</span></span><a href="#l650"></a>
<span id="l651"><span class="sd">        them as a list of `Example` objects.  Line numbers are</span></span><a href="#l651"></a>
<span id="l652"><span class="sd">        0-based, because it&#39;s most common in doctests that nothing</span></span><a href="#l652"></a>
<span id="l653"><span class="sd">        interesting appears on the same line as opening triple-quote,</span></span><a href="#l653"></a>
<span id="l654"><span class="sd">        and so the first interesting line is called \&quot;line 1\&quot; then.</span></span><a href="#l654"></a>
<span id="l655"></span><a href="#l655"></a>
<span id="l656"><span class="sd">        The optional argument `name` is a name identifying this</span></span><a href="#l656"></a>
<span id="l657"><span class="sd">        string, and is only used for error messages.</span></span><a href="#l657"></a>
<span id="l658"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l658"></a>
<span id="l659">        <span class="k">return</span> <span class="p">[</span><span class="n">x</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">string</span><span class="p">,</span> <span class="n">name</span><span class="p">)</span></span><a href="#l659"></a>
<span id="l660">                <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">Example</span><span class="p">)]</span></span><a href="#l660"></a>
<span id="l661"></span><a href="#l661"></a>
<span id="l662">    <span class="k">def</span> <span class="nf">_parse_example</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">m</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">lineno</span><span class="p">):</span></span><a href="#l662"></a>
<span id="l663">        <span class="sd">&quot;&quot;&quot;</span></span><a href="#l663"></a>
<span id="l664"><span class="sd">        Given a regular expression match from `_EXAMPLE_RE` (`m`),</span></span><a href="#l664"></a>
<span id="l665"><span class="sd">        return a pair `(source, want)`, where `source` is the matched</span></span><a href="#l665"></a>
<span id="l666"><span class="sd">        example&#39;s source code (with prompts and indentation stripped);</span></span><a href="#l666"></a>
<span id="l667"><span class="sd">        and `want` is the example&#39;s expected output (with indentation</span></span><a href="#l667"></a>
<span id="l668"><span class="sd">        stripped).</span></span><a href="#l668"></a>
<span id="l669"></span><a href="#l669"></a>
<span id="l670"><span class="sd">        `name` is the string&#39;s name, and `lineno` is the line number</span></span><a href="#l670"></a>
<span id="l671"><span class="sd">        where the example starts; both are used for error messages.</span></span><a href="#l671"></a>
<span id="l672"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l672"></a>
<span id="l673">        <span class="c"># Get the example&#39;s indentation level.</span></span><a href="#l673"></a>
<span id="l674">        <span class="n">indent</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">m</span><span class="o">.</span><span class="n">group</span><span class="p">(</span><span class="s">&#39;indent&#39;</span><span class="p">))</span></span><a href="#l674"></a>
<span id="l675"></span><a href="#l675"></a>
<span id="l676">        <span class="c"># Divide source into lines; check that they&#39;re properly</span></span><a href="#l676"></a>
<span id="l677">        <span class="c"># indented; and then strip their indentation &amp; prompts.</span></span><a href="#l677"></a>
<span id="l678">        <span class="n">source_lines</span> <span class="o">=</span> <span class="n">m</span><span class="o">.</span><span class="n">group</span><span class="p">(</span><span class="s">&#39;source&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span></span><a href="#l678"></a>
<span id="l679">        <span class="bp">self</span><span class="o">.</span><span class="n">_check_prompt_blank</span><span class="p">(</span><span class="n">source_lines</span><span class="p">,</span> <span class="n">indent</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">lineno</span><span class="p">)</span></span><a href="#l679"></a>
<span id="l680">        <span class="bp">self</span><span class="o">.</span><span class="n">_check_prefix</span><span class="p">(</span><span class="n">source_lines</span><span class="p">[</span><span class="mi">1</span><span class="p">:],</span> <span class="s">&#39; &#39;</span><span class="o">*</span><span class="n">indent</span> <span class="o">+</span> <span class="s">&#39;.&#39;</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">lineno</span><span class="p">)</span></span><a href="#l680"></a>
<span id="l681">        <span class="n">source</span> <span class="o">=</span> <span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">sl</span><span class="p">[</span><span class="n">indent</span><span class="o">+</span><span class="mi">4</span><span class="p">:]</span> <span class="k">for</span> <span class="n">sl</span> <span class="ow">in</span> <span class="n">source_lines</span><span class="p">])</span></span><a href="#l681"></a>
<span id="l682"></span><a href="#l682"></a>
<span id="l683">        <span class="c"># Divide want into lines; check that it&#39;s properly indented; and</span></span><a href="#l683"></a>
<span id="l684">        <span class="c"># then strip the indentation.  Spaces before the last newline should</span></span><a href="#l684"></a>
<span id="l685">        <span class="c"># be preserved, so plain rstrip() isn&#39;t good enough.</span></span><a href="#l685"></a>
<span id="l686">        <span class="n">want</span> <span class="o">=</span> <span class="n">m</span><span class="o">.</span><span class="n">group</span><span class="p">(</span><span class="s">&#39;want&#39;</span><span class="p">)</span></span><a href="#l686"></a>
<span id="l687">        <span class="n">want_lines</span> <span class="o">=</span> <span class="n">want</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span></span><a href="#l687"></a>
<span id="l688">        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">want_lines</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span> <span class="ow">and</span> <span class="n">re</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="s">r&#39; *$&#39;</span><span class="p">,</span> <span class="n">want_lines</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]):</span></span><a href="#l688"></a>
<span id="l689">            <span class="k">del</span> <span class="n">want_lines</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>  <span class="c"># forget final newline &amp; spaces after it</span></span><a href="#l689"></a>
<span id="l690">        <span class="bp">self</span><span class="o">.</span><span class="n">_check_prefix</span><span class="p">(</span><span class="n">want_lines</span><span class="p">,</span> <span class="s">&#39; &#39;</span><span class="o">*</span><span class="n">indent</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span></span><a href="#l690"></a>
<span id="l691">                           <span class="n">lineno</span> <span class="o">+</span> <span class="nb">len</span><span class="p">(</span><span class="n">source_lines</span><span class="p">))</span></span><a href="#l691"></a>
<span id="l692">        <span class="n">want</span> <span class="o">=</span> <span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">wl</span><span class="p">[</span><span class="n">indent</span><span class="p">:]</span> <span class="k">for</span> <span class="n">wl</span> <span class="ow">in</span> <span class="n">want_lines</span><span class="p">])</span></span><a href="#l692"></a>
<span id="l693"></span><a href="#l693"></a>
<span id="l694">        <span class="c"># If `want` contains a traceback message, then extract it.</span></span><a href="#l694"></a>
<span id="l695">        <span class="n">m</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_EXCEPTION_RE</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="n">want</span><span class="p">)</span></span><a href="#l695"></a>
<span id="l696">        <span class="k">if</span> <span class="n">m</span><span class="p">:</span></span><a href="#l696"></a>
<span id="l697">            <span class="n">exc_msg</span> <span class="o">=</span> <span class="n">m</span><span class="o">.</span><span class="n">group</span><span class="p">(</span><span class="s">&#39;msg&#39;</span><span class="p">)</span></span><a href="#l697"></a>
<span id="l698">        <span class="k">else</span><span class="p">:</span></span><a href="#l698"></a>
<span id="l699">            <span class="n">exc_msg</span> <span class="o">=</span> <span class="bp">None</span></span><a href="#l699"></a>
<span id="l700"></span><a href="#l700"></a>
<span id="l701">        <span class="c"># Extract options from the source.</span></span><a href="#l701"></a>
<span id="l702">        <span class="n">options</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_find_options</span><span class="p">(</span><span class="n">source</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">lineno</span><span class="p">)</span></span><a href="#l702"></a>
<span id="l703"></span><a href="#l703"></a>
<span id="l704">        <span class="k">return</span> <span class="n">source</span><span class="p">,</span> <span class="n">options</span><span class="p">,</span> <span class="n">want</span><span class="p">,</span> <span class="n">exc_msg</span></span><a href="#l704"></a>
<span id="l705"></span><a href="#l705"></a>
<span id="l706">    <span class="c"># This regular expression looks for option directives in the</span></span><a href="#l706"></a>
<span id="l707">    <span class="c"># source code of an example.  Option directives are comments</span></span><a href="#l707"></a>
<span id="l708">    <span class="c"># starting with &quot;doctest:&quot;.  Warning: this may give false</span></span><a href="#l708"></a>
<span id="l709">    <span class="c"># positives for string-literals that contain the string</span></span><a href="#l709"></a>
<span id="l710">    <span class="c"># &quot;#doctest:&quot;.  Eliminating these false positives would require</span></span><a href="#l710"></a>
<span id="l711">    <span class="c"># actually parsing the string; but we limit them by ignoring any</span></span><a href="#l711"></a>
<span id="l712">    <span class="c"># line containing &quot;#doctest:&quot; that is *followed* by a quote mark.</span></span><a href="#l712"></a>
<span id="l713">    <span class="n">_OPTION_DIRECTIVE_RE</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="s">r&#39;#\s*doctest:\s*([^\n</span><span class="se">\&#39;</span><span class="s">&quot;]*)$&#39;</span><span class="p">,</span></span><a href="#l713"></a>
<span id="l714">                                      <span class="n">re</span><span class="o">.</span><span class="n">MULTILINE</span><span class="p">)</span></span><a href="#l714"></a>
<span id="l715"></span><a href="#l715"></a>
<span id="l716">    <span class="k">def</span> <span class="nf">_find_options</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">source</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">lineno</span><span class="p">):</span></span><a href="#l716"></a>
<span id="l717">        <span class="sd">&quot;&quot;&quot;</span></span><a href="#l717"></a>
<span id="l718"><span class="sd">        Return a dictionary containing option overrides extracted from</span></span><a href="#l718"></a>
<span id="l719"><span class="sd">        option directives in the given source string.</span></span><a href="#l719"></a>
<span id="l720"></span><a href="#l720"></a>
<span id="l721"><span class="sd">        `name` is the string&#39;s name, and `lineno` is the line number</span></span><a href="#l721"></a>
<span id="l722"><span class="sd">        where the example starts; both are used for error messages.</span></span><a href="#l722"></a>
<span id="l723"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l723"></a>
<span id="l724">        <span class="n">options</span> <span class="o">=</span> <span class="p">{}</span></span><a href="#l724"></a>
<span id="l725">        <span class="c"># (note: with the current regexp, this will match at most once:)</span></span><a href="#l725"></a>
<span id="l726">        <span class="k">for</span> <span class="n">m</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_OPTION_DIRECTIVE_RE</span><span class="o">.</span><span class="n">finditer</span><span class="p">(</span><span class="n">source</span><span class="p">):</span></span><a href="#l726"></a>
<span id="l727">            <span class="n">option_strings</span> <span class="o">=</span> <span class="n">m</span><span class="o">.</span><span class="n">group</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&#39;,&#39;</span><span class="p">,</span> <span class="s">&#39; &#39;</span><span class="p">)</span><span class="o">.</span><span class="n">split</span><span class="p">()</span></span><a href="#l727"></a>
<span id="l728">            <span class="k">for</span> <span class="n">option</span> <span class="ow">in</span> <span class="n">option_strings</span><span class="p">:</span></span><a href="#l728"></a>
<span id="l729">                <span class="k">if</span> <span class="p">(</span><span class="n">option</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="ow">not</span> <span class="ow">in</span> <span class="s">&#39;+-&#39;</span> <span class="ow">or</span></span><a href="#l729"></a>
<span id="l730">                    <span class="n">option</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">OPTIONFLAGS_BY_NAME</span><span class="p">):</span></span><a href="#l730"></a>
<span id="l731">                    <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&#39;line </span><span class="si">%r</span><span class="s"> of the doctest for </span><span class="si">%s</span><span class="s"> &#39;</span></span><a href="#l731"></a>
<span id="l732">                                     <span class="s">&#39;has an invalid option: </span><span class="si">%r</span><span class="s">&#39;</span> <span class="o">%</span></span><a href="#l732"></a>
<span id="l733">                                     <span class="p">(</span><span class="n">lineno</span><span class="o">+</span><span class="mi">1</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">option</span><span class="p">))</span></span><a href="#l733"></a>
<span id="l734">                <span class="n">flag</span> <span class="o">=</span> <span class="n">OPTIONFLAGS_BY_NAME</span><span class="p">[</span><span class="n">option</span><span class="p">[</span><span class="mi">1</span><span class="p">:]]</span></span><a href="#l734"></a>
<span id="l735">                <span class="n">options</span><span class="p">[</span><span class="n">flag</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">option</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">==</span> <span class="s">&#39;+&#39;</span><span class="p">)</span></span><a href="#l735"></a>
<span id="l736">        <span class="k">if</span> <span class="n">options</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">_IS_BLANK_OR_COMMENT</span><span class="p">(</span><span class="n">source</span><span class="p">):</span></span><a href="#l736"></a>
<span id="l737">            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&#39;line </span><span class="si">%r</span><span class="s"> of the doctest for </span><span class="si">%s</span><span class="s"> has an option &#39;</span></span><a href="#l737"></a>
<span id="l738">                             <span class="s">&#39;directive on a line with no example: </span><span class="si">%r</span><span class="s">&#39;</span> <span class="o">%</span></span><a href="#l738"></a>
<span id="l739">                             <span class="p">(</span><span class="n">lineno</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">source</span><span class="p">))</span></span><a href="#l739"></a>
<span id="l740">        <span class="k">return</span> <span class="n">options</span></span><a href="#l740"></a>
<span id="l741"></span><a href="#l741"></a>
<span id="l742">    <span class="c"># This regular expression finds the indentation of every non-blank</span></span><a href="#l742"></a>
<span id="l743">    <span class="c"># line in a string.</span></span><a href="#l743"></a>
<span id="l744">    <span class="n">_INDENT_RE</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="s">&#39;^([ ]*)(?=\S)&#39;</span><span class="p">,</span> <span class="n">re</span><span class="o">.</span><span class="n">MULTILINE</span><span class="p">)</span></span><a href="#l744"></a>
<span id="l745"></span><a href="#l745"></a>
<span id="l746">    <span class="k">def</span> <span class="nf">_min_indent</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">s</span><span class="p">):</span></span><a href="#l746"></a>
<span id="l747">        <span class="s">&quot;Return the minimum indentation of any non-blank line in `s`&quot;</span></span><a href="#l747"></a>
<span id="l748">        <span class="n">indents</span> <span class="o">=</span> <span class="p">[</span><span class="nb">len</span><span class="p">(</span><span class="n">indent</span><span class="p">)</span> <span class="k">for</span> <span class="n">indent</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_INDENT_RE</span><span class="o">.</span><span class="n">findall</span><span class="p">(</span><span class="n">s</span><span class="p">)]</span></span><a href="#l748"></a>
<span id="l749">        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">indents</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span></span><a href="#l749"></a>
<span id="l750">            <span class="k">return</span> <span class="nb">min</span><span class="p">(</span><span class="n">indents</span><span class="p">)</span></span><a href="#l750"></a>
<span id="l751">        <span class="k">else</span><span class="p">:</span></span><a href="#l751"></a>
<span id="l752">            <span class="k">return</span> <span class="mi">0</span></span><a href="#l752"></a>
<span id="l753"></span><a href="#l753"></a>
<span id="l754">    <span class="k">def</span> <span class="nf">_check_prompt_blank</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">lines</span><span class="p">,</span> <span class="n">indent</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">lineno</span><span class="p">):</span></span><a href="#l754"></a>
<span id="l755">        <span class="sd">&quot;&quot;&quot;</span></span><a href="#l755"></a>
<span id="l756"><span class="sd">        Given the lines of a source string (including prompts and</span></span><a href="#l756"></a>
<span id="l757"><span class="sd">        leading indentation), check to make sure that every prompt is</span></span><a href="#l757"></a>
<span id="l758"><span class="sd">        followed by a space character.  If any line is not followed by</span></span><a href="#l758"></a>
<span id="l759"><span class="sd">        a space character, then raise ValueError.</span></span><a href="#l759"></a>
<span id="l760"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l760"></a>
<span id="l761">        <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">line</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">lines</span><span class="p">):</span></span><a href="#l761"></a>
<span id="l762">            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">line</span><span class="p">)</span> <span class="o">&gt;=</span> <span class="n">indent</span><span class="o">+</span><span class="mi">4</span> <span class="ow">and</span> <span class="n">line</span><span class="p">[</span><span class="n">indent</span><span class="o">+</span><span class="mi">3</span><span class="p">]</span> <span class="o">!=</span> <span class="s">&#39; &#39;</span><span class="p">:</span></span><a href="#l762"></a>
<span id="l763">                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&#39;line </span><span class="si">%r</span><span class="s"> of the docstring for </span><span class="si">%s</span><span class="s"> &#39;</span></span><a href="#l763"></a>
<span id="l764">                                 <span class="s">&#39;lacks blank after </span><span class="si">%s</span><span class="s">: </span><span class="si">%r</span><span class="s">&#39;</span> <span class="o">%</span></span><a href="#l764"></a>
<span id="l765">                                 <span class="p">(</span><span class="n">lineno</span><span class="o">+</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span></span><a href="#l765"></a>
<span id="l766">                                  <span class="n">line</span><span class="p">[</span><span class="n">indent</span><span class="p">:</span><span class="n">indent</span><span class="o">+</span><span class="mi">3</span><span class="p">],</span> <span class="n">line</span><span class="p">))</span></span><a href="#l766"></a>
<span id="l767"></span><a href="#l767"></a>
<span id="l768">    <span class="k">def</span> <span class="nf">_check_prefix</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">lines</span><span class="p">,</span> <span class="n">prefix</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">lineno</span><span class="p">):</span></span><a href="#l768"></a>
<span id="l769">        <span class="sd">&quot;&quot;&quot;</span></span><a href="#l769"></a>
<span id="l770"><span class="sd">        Check that every line in the given list starts with the given</span></span><a href="#l770"></a>
<span id="l771"><span class="sd">        prefix; if any line does not, then raise a ValueError.</span></span><a href="#l771"></a>
<span id="l772"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l772"></a>
<span id="l773">        <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">line</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">lines</span><span class="p">):</span></span><a href="#l773"></a>
<span id="l774">            <span class="k">if</span> <span class="n">line</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">line</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="n">prefix</span><span class="p">):</span></span><a href="#l774"></a>
<span id="l775">                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&#39;line </span><span class="si">%r</span><span class="s"> of the docstring for </span><span class="si">%s</span><span class="s"> has &#39;</span></span><a href="#l775"></a>
<span id="l776">                                 <span class="s">&#39;inconsistent leading whitespace: </span><span class="si">%r</span><span class="s">&#39;</span> <span class="o">%</span></span><a href="#l776"></a>
<span id="l777">                                 <span class="p">(</span><span class="n">lineno</span><span class="o">+</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">line</span><span class="p">))</span></span><a href="#l777"></a>
<span id="l778"></span><a href="#l778"></a>
<span id="l779"></span><a href="#l779"></a>
<span id="l780"><span class="c">######################################################################</span></span><a href="#l780"></a>
<span id="l781"><span class="c">## 4. DocTest Finder</span></span><a href="#l781"></a>
<span id="l782"><span class="c">######################################################################</span></span><a href="#l782"></a>
<span id="l783"></span><a href="#l783"></a>
<span id="l784"><span class="k">class</span> <span class="nc">DocTestFinder</span><span class="p">:</span></span><a href="#l784"></a>
<span id="l785">    <span class="sd">&quot;&quot;&quot;</span></span><a href="#l785"></a>
<span id="l786"><span class="sd">    A class used to extract the DocTests that are relevant to a given</span></span><a href="#l786"></a>
<span id="l787"><span class="sd">    object, from its docstring and the docstrings of its contained</span></span><a href="#l787"></a>
<span id="l788"><span class="sd">    objects.  Doctests can currently be extracted from the following</span></span><a href="#l788"></a>
<span id="l789"><span class="sd">    object types: modules, functions, classes, methods, staticmethods,</span></span><a href="#l789"></a>
<span id="l790"><span class="sd">    classmethods, and properties.</span></span><a href="#l790"></a>
<span id="l791"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l791"></a>
<span id="l792"></span><a href="#l792"></a>
<span id="l793">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">verbose</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span> <span class="n">parser</span><span class="o">=</span><span class="n">DocTestParser</span><span class="p">(),</span></span><a href="#l793"></a>
<span id="l794">                 <span class="n">recurse</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span> <span class="n">exclude_empty</span><span class="o">=</span><span class="bp">True</span><span class="p">):</span></span><a href="#l794"></a>
<span id="l795">        <span class="sd">&quot;&quot;&quot;</span></span><a href="#l795"></a>
<span id="l796"><span class="sd">        Create a new doctest finder.</span></span><a href="#l796"></a>
<span id="l797"></span><a href="#l797"></a>
<span id="l798"><span class="sd">        The optional argument `parser` specifies a class or</span></span><a href="#l798"></a>
<span id="l799"><span class="sd">        function that should be used to create new DocTest objects (or</span></span><a href="#l799"></a>
<span id="l800"><span class="sd">        objects that implement the same interface as DocTest).  The</span></span><a href="#l800"></a>
<span id="l801"><span class="sd">        signature for this factory function should match the signature</span></span><a href="#l801"></a>
<span id="l802"><span class="sd">        of the DocTest constructor.</span></span><a href="#l802"></a>
<span id="l803"></span><a href="#l803"></a>
<span id="l804"><span class="sd">        If the optional argument `recurse` is false, then `find` will</span></span><a href="#l804"></a>
<span id="l805"><span class="sd">        only examine the given object, and not any contained objects.</span></span><a href="#l805"></a>
<span id="l806"></span><a href="#l806"></a>
<span id="l807"><span class="sd">        If the optional argument `exclude_empty` is false, then `find`</span></span><a href="#l807"></a>
<span id="l808"><span class="sd">        will include tests for objects with empty docstrings.</span></span><a href="#l808"></a>
<span id="l809"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l809"></a>
<span id="l810">        <span class="bp">self</span><span class="o">.</span><span class="n">_parser</span> <span class="o">=</span> <span class="n">parser</span></span><a href="#l810"></a>
<span id="l811">        <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span> <span class="o">=</span> <span class="n">verbose</span></span><a href="#l811"></a>
<span id="l812">        <span class="bp">self</span><span class="o">.</span><span class="n">_recurse</span> <span class="o">=</span> <span class="n">recurse</span></span><a href="#l812"></a>
<span id="l813">        <span class="bp">self</span><span class="o">.</span><span class="n">_exclude_empty</span> <span class="o">=</span> <span class="n">exclude_empty</span></span><a href="#l813"></a>
<span id="l814"></span><a href="#l814"></a>
<span id="l815">    <span class="k">def</span> <span class="nf">find</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">module</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">globs</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">extraglobs</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l815"></a>
<span id="l816">        <span class="sd">&quot;&quot;&quot;</span></span><a href="#l816"></a>
<span id="l817"><span class="sd">        Return a list of the DocTests that are defined by the given</span></span><a href="#l817"></a>
<span id="l818"><span class="sd">        object&#39;s docstring, or by any of its contained objects&#39;</span></span><a href="#l818"></a>
<span id="l819"><span class="sd">        docstrings.</span></span><a href="#l819"></a>
<span id="l820"></span><a href="#l820"></a>
<span id="l821"><span class="sd">        The optional parameter `module` is the module that contains</span></span><a href="#l821"></a>
<span id="l822"><span class="sd">        the given object.  If the module is not specified or is None, then</span></span><a href="#l822"></a>
<span id="l823"><span class="sd">        the test finder will attempt to automatically determine the</span></span><a href="#l823"></a>
<span id="l824"><span class="sd">        correct module.  The object&#39;s module is used:</span></span><a href="#l824"></a>
<span id="l825"></span><a href="#l825"></a>
<span id="l826"><span class="sd">            - As a default namespace, if `globs` is not specified.</span></span><a href="#l826"></a>
<span id="l827"><span class="sd">            - To prevent the DocTestFinder from extracting DocTests</span></span><a href="#l827"></a>
<span id="l828"><span class="sd">              from objects that are imported from other modules.</span></span><a href="#l828"></a>
<span id="l829"><span class="sd">            - To find the name of the file containing the object.</span></span><a href="#l829"></a>
<span id="l830"><span class="sd">            - To help find the line number of the object within its</span></span><a href="#l830"></a>
<span id="l831"><span class="sd">              file.</span></span><a href="#l831"></a>
<span id="l832"></span><a href="#l832"></a>
<span id="l833"><span class="sd">        Contained objects whose module does not match `module` are ignored.</span></span><a href="#l833"></a>
<span id="l834"></span><a href="#l834"></a>
<span id="l835"><span class="sd">        If `module` is False, no attempt to find the module will be made.</span></span><a href="#l835"></a>
<span id="l836"><span class="sd">        This is obscure, of use mostly in tests:  if `module` is False, or</span></span><a href="#l836"></a>
<span id="l837"><span class="sd">        is None but cannot be found automatically, then all objects are</span></span><a href="#l837"></a>
<span id="l838"><span class="sd">        considered to belong to the (non-existent) module, so all contained</span></span><a href="#l838"></a>
<span id="l839"><span class="sd">        objects will (recursively) be searched for doctests.</span></span><a href="#l839"></a>
<span id="l840"></span><a href="#l840"></a>
<span id="l841"><span class="sd">        The globals for each DocTest is formed by combining `globs`</span></span><a href="#l841"></a>
<span id="l842"><span class="sd">        and `extraglobs` (bindings in `extraglobs` override bindings</span></span><a href="#l842"></a>
<span id="l843"><span class="sd">        in `globs`).  A new copy of the globals dictionary is created</span></span><a href="#l843"></a>
<span id="l844"><span class="sd">        for each DocTest.  If `globs` is not specified, then it</span></span><a href="#l844"></a>
<span id="l845"><span class="sd">        defaults to the module&#39;s `__dict__`, if specified, or {}</span></span><a href="#l845"></a>
<span id="l846"><span class="sd">        otherwise.  If `extraglobs` is not specified, then it defaults</span></span><a href="#l846"></a>
<span id="l847"><span class="sd">        to {}.</span></span><a href="#l847"></a>
<span id="l848"></span><a href="#l848"></a>
<span id="l849"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l849"></a>
<span id="l850">        <span class="c"># If name was not specified, then extract it from the object.</span></span><a href="#l850"></a>
<span id="l851">        <span class="k">if</span> <span class="n">name</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l851"></a>
<span id="l852">            <span class="n">name</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="s">&#39;__name__&#39;</span><span class="p">,</span> <span class="bp">None</span><span class="p">)</span></span><a href="#l852"></a>
<span id="l853">            <span class="k">if</span> <span class="n">name</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l853"></a>
<span id="l854">                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&quot;DocTestFinder.find: name must be given &quot;</span></span><a href="#l854"></a>
<span id="l855">                        <span class="s">&quot;when obj.__name__ doesn&#39;t exist: </span><span class="si">%r</span><span class="s">&quot;</span> <span class="o">%</span></span><a href="#l855"></a>
<span id="l856">                                 <span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="n">obj</span><span class="p">),))</span></span><a href="#l856"></a>
<span id="l857"></span><a href="#l857"></a>
<span id="l858">        <span class="c"># Find the module that contains the given object (if obj is</span></span><a href="#l858"></a>
<span id="l859">        <span class="c"># a module, then module=obj.).  Note: this may fail, in which</span></span><a href="#l859"></a>
<span id="l860">        <span class="c"># case module will be None.</span></span><a href="#l860"></a>
<span id="l861">        <span class="k">if</span> <span class="n">module</span> <span class="ow">is</span> <span class="bp">False</span><span class="p">:</span></span><a href="#l861"></a>
<span id="l862">            <span class="n">module</span> <span class="o">=</span> <span class="bp">None</span></span><a href="#l862"></a>
<span id="l863">        <span class="k">elif</span> <span class="n">module</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l863"></a>
<span id="l864">            <span class="n">module</span> <span class="o">=</span> <span class="n">inspect</span><span class="o">.</span><span class="n">getmodule</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span></span><a href="#l864"></a>
<span id="l865"></span><a href="#l865"></a>
<span id="l866">        <span class="c"># Read the module&#39;s source code.  This is used by</span></span><a href="#l866"></a>
<span id="l867">        <span class="c"># DocTestFinder._find_lineno to find the line number for a</span></span><a href="#l867"></a>
<span id="l868">        <span class="c"># given object&#39;s docstring.</span></span><a href="#l868"></a>
<span id="l869">        <span class="k">try</span><span class="p">:</span></span><a href="#l869"></a>
<span id="l870">            <span class="nb">file</span> <span class="o">=</span> <span class="n">inspect</span><span class="o">.</span><span class="n">getsourcefile</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span> <span class="ow">or</span> <span class="n">inspect</span><span class="o">.</span><span class="n">getfile</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span></span><a href="#l870"></a>
<span id="l871">            <span class="k">if</span> <span class="n">module</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l871"></a>
<span id="l872">                <span class="c"># Supply the module globals in case the module was</span></span><a href="#l872"></a>
<span id="l873">                <span class="c"># originally loaded via a PEP 302 loader and</span></span><a href="#l873"></a>
<span id="l874">                <span class="c"># file is not a valid filesystem path</span></span><a href="#l874"></a>
<span id="l875">                <span class="n">source_lines</span> <span class="o">=</span> <span class="n">linecache</span><span class="o">.</span><span class="n">getlines</span><span class="p">(</span><span class="nb">file</span><span class="p">,</span> <span class="n">module</span><span class="o">.</span><span class="n">__dict__</span><span class="p">)</span></span><a href="#l875"></a>
<span id="l876">            <span class="k">else</span><span class="p">:</span></span><a href="#l876"></a>
<span id="l877">                <span class="c"># No access to a loader, so assume it&#39;s a normal</span></span><a href="#l877"></a>
<span id="l878">                <span class="c"># filesystem path</span></span><a href="#l878"></a>
<span id="l879">                <span class="n">source_lines</span> <span class="o">=</span> <span class="n">linecache</span><span class="o">.</span><span class="n">getlines</span><span class="p">(</span><span class="nb">file</span><span class="p">)</span></span><a href="#l879"></a>
<span id="l880">            <span class="k">if</span> <span class="ow">not</span> <span class="n">source_lines</span><span class="p">:</span></span><a href="#l880"></a>
<span id="l881">                <span class="n">source_lines</span> <span class="o">=</span> <span class="bp">None</span></span><a href="#l881"></a>
<span id="l882">        <span class="k">except</span> <span class="ne">TypeError</span><span class="p">:</span></span><a href="#l882"></a>
<span id="l883">            <span class="n">source_lines</span> <span class="o">=</span> <span class="bp">None</span></span><a href="#l883"></a>
<span id="l884"></span><a href="#l884"></a>
<span id="l885">        <span class="c"># Initialize globals, and merge in extraglobs.</span></span><a href="#l885"></a>
<span id="l886">        <span class="k">if</span> <span class="n">globs</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l886"></a>
<span id="l887">            <span class="k">if</span> <span class="n">module</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l887"></a>
<span id="l888">                <span class="n">globs</span> <span class="o">=</span> <span class="p">{}</span></span><a href="#l888"></a>
<span id="l889">            <span class="k">else</span><span class="p">:</span></span><a href="#l889"></a>
<span id="l890">                <span class="n">globs</span> <span class="o">=</span> <span class="n">module</span><span class="o">.</span><span class="n">__dict__</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span></span><a href="#l890"></a>
<span id="l891">        <span class="k">else</span><span class="p">:</span></span><a href="#l891"></a>
<span id="l892">            <span class="n">globs</span> <span class="o">=</span> <span class="n">globs</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span></span><a href="#l892"></a>
<span id="l893">        <span class="k">if</span> <span class="n">extraglobs</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l893"></a>
<span id="l894">            <span class="n">globs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">extraglobs</span><span class="p">)</span></span><a href="#l894"></a>
<span id="l895">        <span class="k">if</span> <span class="s">&#39;__name__&#39;</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">globs</span><span class="p">:</span></span><a href="#l895"></a>
<span id="l896">            <span class="n">globs</span><span class="p">[</span><span class="s">&#39;__name__&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="s">&#39;__main__&#39;</span>  <span class="c"># provide a default module name</span></span><a href="#l896"></a>
<span id="l897"></span><a href="#l897"></a>
<span id="l898">        <span class="c"># Recursively expore `obj`, extracting DocTests.</span></span><a href="#l898"></a>
<span id="l899">        <span class="n">tests</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l899"></a>
<span id="l900">        <span class="bp">self</span><span class="o">.</span><span class="n">_find</span><span class="p">(</span><span class="n">tests</span><span class="p">,</span> <span class="n">obj</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">module</span><span class="p">,</span> <span class="n">source_lines</span><span class="p">,</span> <span class="n">globs</span><span class="p">,</span> <span class="p">{})</span></span><a href="#l900"></a>
<span id="l901">        <span class="c"># Sort the tests by alpha order of names, for consistency in</span></span><a href="#l901"></a>
<span id="l902">        <span class="c"># verbose-mode output.  This was a feature of doctest in Pythons</span></span><a href="#l902"></a>
<span id="l903">        <span class="c"># &lt;= 2.3 that got lost by accident in 2.4.  It was repaired in</span></span><a href="#l903"></a>
<span id="l904">        <span class="c"># 2.4.4 and 2.5.</span></span><a href="#l904"></a>
<span id="l905">        <span class="n">tests</span><span class="o">.</span><span class="n">sort</span><span class="p">()</span></span><a href="#l905"></a>
<span id="l906">        <span class="k">return</span> <span class="n">tests</span></span><a href="#l906"></a>
<span id="l907"></span><a href="#l907"></a>
<span id="l908">    <span class="k">def</span> <span class="nf">_from_module</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">module</span><span class="p">,</span> <span class="nb">object</span><span class="p">):</span></span><a href="#l908"></a>
<span id="l909">        <span class="sd">&quot;&quot;&quot;</span></span><a href="#l909"></a>
<span id="l910"><span class="sd">        Return true if the given object is defined in the given</span></span><a href="#l910"></a>
<span id="l911"><span class="sd">        module.</span></span><a href="#l911"></a>
<span id="l912"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l912"></a>
<span id="l913">        <span class="k">if</span> <span class="n">module</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l913"></a>
<span id="l914">            <span class="k">return</span> <span class="bp">True</span></span><a href="#l914"></a>
<span id="l915">        <span class="k">elif</span> <span class="n">inspect</span><span class="o">.</span><span class="n">getmodule</span><span class="p">(</span><span class="nb">object</span><span class="p">)</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l915"></a>
<span id="l916">            <span class="k">return</span> <span class="n">module</span> <span class="ow">is</span> <span class="n">inspect</span><span class="o">.</span><span class="n">getmodule</span><span class="p">(</span><span class="nb">object</span><span class="p">)</span></span><a href="#l916"></a>
<span id="l917">        <span class="k">elif</span> <span class="n">inspect</span><span class="o">.</span><span class="n">isfunction</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></span><a href="#l917"></a>
<span id="l918">            <span class="k">return</span> <span class="n">module</span><span class="o">.</span><span class="n">__dict__</span> <span class="ow">is</span> <span class="nb">object</span><span class="o">.</span><span class="n">func_globals</span></span><a href="#l918"></a>
<span id="l919">        <span class="k">elif</span> <span class="n">inspect</span><span class="o">.</span><span class="n">isclass</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></span><a href="#l919"></a>
<span id="l920">            <span class="k">return</span> <span class="n">module</span><span class="o">.</span><span class="n">__name__</span> <span class="o">==</span> <span class="nb">object</span><span class="o">.</span><span class="n">__module__</span></span><a href="#l920"></a>
<span id="l921">        <span class="k">elif</span> <span class="nb">hasattr</span><span class="p">(</span><span class="nb">object</span><span class="p">,</span> <span class="s">&#39;__module__&#39;</span><span class="p">):</span></span><a href="#l921"></a>
<span id="l922">            <span class="k">return</span> <span class="n">module</span><span class="o">.</span><span class="n">__name__</span> <span class="o">==</span> <span class="nb">object</span><span class="o">.</span><span class="n">__module__</span></span><a href="#l922"></a>
<span id="l923">        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="nb">object</span><span class="p">,</span> <span class="nb">property</span><span class="p">):</span></span><a href="#l923"></a>
<span id="l924">            <span class="k">return</span> <span class="bp">True</span> <span class="c"># [XX] no way not be sure.</span></span><a href="#l924"></a>
<span id="l925">        <span class="k">else</span><span class="p">:</span></span><a href="#l925"></a>
<span id="l926">            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&quot;object must be a class or function&quot;</span><span class="p">)</span></span><a href="#l926"></a>
<span id="l927"></span><a href="#l927"></a>
<span id="l928">    <span class="k">def</span> <span class="nf">_find</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tests</span><span class="p">,</span> <span class="n">obj</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">module</span><span class="p">,</span> <span class="n">source_lines</span><span class="p">,</span> <span class="n">globs</span><span class="p">,</span> <span class="n">seen</span><span class="p">):</span></span><a href="#l928"></a>
<span id="l929">        <span class="sd">&quot;&quot;&quot;</span></span><a href="#l929"></a>
<span id="l930"><span class="sd">        Find tests for the given object and any contained objects, and</span></span><a href="#l930"></a>
<span id="l931"><span class="sd">        add them to `tests`.</span></span><a href="#l931"></a>
<span id="l932"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l932"></a>
<span id="l933">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span></span><a href="#l933"></a>
<span id="l934">            <span class="k">print</span> <span class="s">&#39;Finding tests in </span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">name</span></span><a href="#l934"></a>
<span id="l935"></span><a href="#l935"></a>
<span id="l936">        <span class="c"># If we&#39;ve already processed this object, then ignore it.</span></span><a href="#l936"></a>
<span id="l937">        <span class="k">if</span> <span class="nb">id</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span> <span class="ow">in</span> <span class="n">seen</span><span class="p">:</span></span><a href="#l937"></a>
<span id="l938">            <span class="k">return</span></span><a href="#l938"></a>
<span id="l939">        <span class="n">seen</span><span class="p">[</span><span class="nb">id</span><span class="p">(</span><span class="n">obj</span><span class="p">)]</span> <span class="o">=</span> <span class="mi">1</span></span><a href="#l939"></a>
<span id="l940"></span><a href="#l940"></a>
<span id="l941">        <span class="c"># Find a test for this object, and add it to the list of tests.</span></span><a href="#l941"></a>
<span id="l942">        <span class="n">test</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_test</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">module</span><span class="p">,</span> <span class="n">globs</span><span class="p">,</span> <span class="n">source_lines</span><span class="p">)</span></span><a href="#l942"></a>
<span id="l943">        <span class="k">if</span> <span class="n">test</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l943"></a>
<span id="l944">            <span class="n">tests</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">test</span><span class="p">)</span></span><a href="#l944"></a>
<span id="l945"></span><a href="#l945"></a>
<span id="l946">        <span class="c"># Look for tests in a module&#39;s contained objects.</span></span><a href="#l946"></a>
<span id="l947">        <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">ismodule</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">_recurse</span><span class="p">:</span></span><a href="#l947"></a>
<span id="l948">            <span class="k">for</span> <span class="n">valname</span><span class="p">,</span> <span class="n">val</span> <span class="ow">in</span> <span class="n">obj</span><span class="o">.</span><span class="n">__dict__</span><span class="o">.</span><span class="n">items</span><span class="p">():</span></span><a href="#l948"></a>
<span id="l949">                <span class="n">valname</span> <span class="o">=</span> <span class="s">&#39;</span><span class="si">%s</span><span class="s">.</span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">valname</span><span class="p">)</span></span><a href="#l949"></a>
<span id="l950">                <span class="c"># Recurse to functions &amp; classes.</span></span><a href="#l950"></a>
<span id="l951">                <span class="k">if</span> <span class="p">((</span><span class="n">inspect</span><span class="o">.</span><span class="n">isfunction</span><span class="p">(</span><span class="n">val</span><span class="p">)</span> <span class="ow">or</span> <span class="n">inspect</span><span class="o">.</span><span class="n">isclass</span><span class="p">(</span><span class="n">val</span><span class="p">))</span> <span class="ow">and</span></span><a href="#l951"></a>
<span id="l952">                    <span class="bp">self</span><span class="o">.</span><span class="n">_from_module</span><span class="p">(</span><span class="n">module</span><span class="p">,</span> <span class="n">val</span><span class="p">)):</span></span><a href="#l952"></a>
<span id="l953">                    <span class="bp">self</span><span class="o">.</span><span class="n">_find</span><span class="p">(</span><span class="n">tests</span><span class="p">,</span> <span class="n">val</span><span class="p">,</span> <span class="n">valname</span><span class="p">,</span> <span class="n">module</span><span class="p">,</span> <span class="n">source_lines</span><span class="p">,</span></span><a href="#l953"></a>
<span id="l954">                               <span class="n">globs</span><span class="p">,</span> <span class="n">seen</span><span class="p">)</span></span><a href="#l954"></a>
<span id="l955"></span><a href="#l955"></a>
<span id="l956">        <span class="c"># Look for tests in a module&#39;s __test__ dictionary.</span></span><a href="#l956"></a>
<span id="l957">        <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">ismodule</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">_recurse</span><span class="p">:</span></span><a href="#l957"></a>
<span id="l958">            <span class="k">for</span> <span class="n">valname</span><span class="p">,</span> <span class="n">val</span> <span class="ow">in</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="s">&#39;__test__&#39;</span><span class="p">,</span> <span class="p">{})</span><span class="o">.</span><span class="n">items</span><span class="p">():</span></span><a href="#l958"></a>
<span id="l959">                <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">valname</span><span class="p">,</span> <span class="nb">basestring</span><span class="p">):</span></span><a href="#l959"></a>
<span id="l960">                    <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&quot;DocTestFinder.find: __test__ keys &quot;</span></span><a href="#l960"></a>
<span id="l961">                                     <span class="s">&quot;must be strings: </span><span class="si">%r</span><span class="s">&quot;</span> <span class="o">%</span></span><a href="#l961"></a>
<span id="l962">                                     <span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="n">valname</span><span class="p">),))</span></span><a href="#l962"></a>
<span id="l963">                <span class="k">if</span> <span class="ow">not</span> <span class="p">(</span><span class="n">inspect</span><span class="o">.</span><span class="n">isfunction</span><span class="p">(</span><span class="n">val</span><span class="p">)</span> <span class="ow">or</span> <span class="n">inspect</span><span class="o">.</span><span class="n">isclass</span><span class="p">(</span><span class="n">val</span><span class="p">)</span> <span class="ow">or</span></span><a href="#l963"></a>
<span id="l964">                        <span class="n">inspect</span><span class="o">.</span><span class="n">ismethod</span><span class="p">(</span><span class="n">val</span><span class="p">)</span> <span class="ow">or</span> <span class="n">inspect</span><span class="o">.</span><span class="n">ismodule</span><span class="p">(</span><span class="n">val</span><span class="p">)</span> <span class="ow">or</span></span><a href="#l964"></a>
<span id="l965">                        <span class="nb">isinstance</span><span class="p">(</span><span class="n">val</span><span class="p">,</span> <span class="nb">basestring</span><span class="p">)):</span></span><a href="#l965"></a>
<span id="l966">                    <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&quot;DocTestFinder.find: __test__ values &quot;</span></span><a href="#l966"></a>
<span id="l967">                                     <span class="s">&quot;must be strings, functions, methods, &quot;</span></span><a href="#l967"></a>
<span id="l968">                                     <span class="s">&quot;classes, or modules: </span><span class="si">%r</span><span class="s">&quot;</span> <span class="o">%</span></span><a href="#l968"></a>
<span id="l969">                                     <span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="n">val</span><span class="p">),))</span></span><a href="#l969"></a>
<span id="l970">                <span class="n">valname</span> <span class="o">=</span> <span class="s">&#39;</span><span class="si">%s</span><span class="s">.__test__.</span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">valname</span><span class="p">)</span></span><a href="#l970"></a>
<span id="l971">                <span class="bp">self</span><span class="o">.</span><span class="n">_find</span><span class="p">(</span><span class="n">tests</span><span class="p">,</span> <span class="n">val</span><span class="p">,</span> <span class="n">valname</span><span class="p">,</span> <span class="n">module</span><span class="p">,</span> <span class="n">source_lines</span><span class="p">,</span></span><a href="#l971"></a>
<span id="l972">                           <span class="n">globs</span><span class="p">,</span> <span class="n">seen</span><span class="p">)</span></span><a href="#l972"></a>
<span id="l973"></span><a href="#l973"></a>
<span id="l974">        <span class="c"># Look for tests in a class&#39;s contained objects.</span></span><a href="#l974"></a>
<span id="l975">        <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">isclass</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">_recurse</span><span class="p">:</span></span><a href="#l975"></a>
<span id="l976">            <span class="k">for</span> <span class="n">valname</span><span class="p">,</span> <span class="n">val</span> <span class="ow">in</span> <span class="n">obj</span><span class="o">.</span><span class="n">__dict__</span><span class="o">.</span><span class="n">items</span><span class="p">():</span></span><a href="#l976"></a>
<span id="l977">                <span class="c"># Special handling for staticmethod/classmethod.</span></span><a href="#l977"></a>
<span id="l978">                <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">val</span><span class="p">,</span> <span class="nb">staticmethod</span><span class="p">):</span></span><a href="#l978"></a>
<span id="l979">                    <span class="n">val</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">valname</span><span class="p">)</span></span><a href="#l979"></a>
<span id="l980">                <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">val</span><span class="p">,</span> <span class="nb">classmethod</span><span class="p">):</span></span><a href="#l980"></a>
<span id="l981">                    <span class="n">val</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">valname</span><span class="p">)</span><span class="o">.</span><span class="n">im_func</span></span><a href="#l981"></a>
<span id="l982"></span><a href="#l982"></a>
<span id="l983">                <span class="c"># Recurse to methods, properties, and nested classes.</span></span><a href="#l983"></a>
<span id="l984">                <span class="k">if</span> <span class="p">((</span><span class="n">inspect</span><span class="o">.</span><span class="n">isfunction</span><span class="p">(</span><span class="n">val</span><span class="p">)</span> <span class="ow">or</span> <span class="n">inspect</span><span class="o">.</span><span class="n">isclass</span><span class="p">(</span><span class="n">val</span><span class="p">)</span> <span class="ow">or</span></span><a href="#l984"></a>
<span id="l985">                      <span class="nb">isinstance</span><span class="p">(</span><span class="n">val</span><span class="p">,</span> <span class="nb">property</span><span class="p">))</span> <span class="ow">and</span></span><a href="#l985"></a>
<span id="l986">                      <span class="bp">self</span><span class="o">.</span><span class="n">_from_module</span><span class="p">(</span><span class="n">module</span><span class="p">,</span> <span class="n">val</span><span class="p">)):</span></span><a href="#l986"></a>
<span id="l987">                    <span class="n">valname</span> <span class="o">=</span> <span class="s">&#39;</span><span class="si">%s</span><span class="s">.</span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">valname</span><span class="p">)</span></span><a href="#l987"></a>
<span id="l988">                    <span class="bp">self</span><span class="o">.</span><span class="n">_find</span><span class="p">(</span><span class="n">tests</span><span class="p">,</span> <span class="n">val</span><span class="p">,</span> <span class="n">valname</span><span class="p">,</span> <span class="n">module</span><span class="p">,</span> <span class="n">source_lines</span><span class="p">,</span></span><a href="#l988"></a>
<span id="l989">                               <span class="n">globs</span><span class="p">,</span> <span class="n">seen</span><span class="p">)</span></span><a href="#l989"></a>
<span id="l990"></span><a href="#l990"></a>
<span id="l991">    <span class="k">def</span> <span class="nf">_get_test</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">module</span><span class="p">,</span> <span class="n">globs</span><span class="p">,</span> <span class="n">source_lines</span><span class="p">):</span></span><a href="#l991"></a>
<span id="l992">        <span class="sd">&quot;&quot;&quot;</span></span><a href="#l992"></a>
<span id="l993"><span class="sd">        Return a DocTest for the given object, if it defines a docstring;</span></span><a href="#l993"></a>
<span id="l994"><span class="sd">        otherwise, return None.</span></span><a href="#l994"></a>
<span id="l995"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l995"></a>
<span id="l996">        <span class="c"># Extract the object&#39;s docstring.  If it doesn&#39;t have one,</span></span><a href="#l996"></a>
<span id="l997">        <span class="c"># then return None (no test for this object).</span></span><a href="#l997"></a>
<span id="l998">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="nb">basestring</span><span class="p">):</span></span><a href="#l998"></a>
<span id="l999">            <span class="n">docstring</span> <span class="o">=</span> <span class="n">obj</span></span><a href="#l999"></a>
<span id="l1000">        <span class="k">else</span><span class="p">:</span></span><a href="#l1000"></a>
<span id="l1001">            <span class="k">try</span><span class="p">:</span></span><a href="#l1001"></a>
<span id="l1002">                <span class="k">if</span> <span class="n">obj</span><span class="o">.</span><span class="n">__doc__</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1002"></a>
<span id="l1003">                    <span class="n">docstring</span> <span class="o">=</span> <span class="s">&#39;&#39;</span></span><a href="#l1003"></a>
<span id="l1004">                <span class="k">else</span><span class="p">:</span></span><a href="#l1004"></a>
<span id="l1005">                    <span class="n">docstring</span> <span class="o">=</span> <span class="n">obj</span><span class="o">.</span><span class="n">__doc__</span></span><a href="#l1005"></a>
<span id="l1006">                    <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">docstring</span><span class="p">,</span> <span class="nb">basestring</span><span class="p">):</span></span><a href="#l1006"></a>
<span id="l1007">                        <span class="n">docstring</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">docstring</span><span class="p">)</span></span><a href="#l1007"></a>
<span id="l1008">            <span class="k">except</span> <span class="p">(</span><span class="ne">TypeError</span><span class="p">,</span> <span class="ne">AttributeError</span><span class="p">):</span></span><a href="#l1008"></a>
<span id="l1009">                <span class="n">docstring</span> <span class="o">=</span> <span class="s">&#39;&#39;</span></span><a href="#l1009"></a>
<span id="l1010"></span><a href="#l1010"></a>
<span id="l1011">        <span class="c"># Find the docstring&#39;s location in the file.</span></span><a href="#l1011"></a>
<span id="l1012">        <span class="n">lineno</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_find_lineno</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">source_lines</span><span class="p">)</span></span><a href="#l1012"></a>
<span id="l1013"></span><a href="#l1013"></a>
<span id="l1014">        <span class="c"># Don&#39;t bother if the docstring is empty.</span></span><a href="#l1014"></a>
<span id="l1015">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exclude_empty</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">docstring</span><span class="p">:</span></span><a href="#l1015"></a>
<span id="l1016">            <span class="k">return</span> <span class="bp">None</span></span><a href="#l1016"></a>
<span id="l1017"></span><a href="#l1017"></a>
<span id="l1018">        <span class="c"># Return a DocTest for this object.</span></span><a href="#l1018"></a>
<span id="l1019">        <span class="k">if</span> <span class="n">module</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1019"></a>
<span id="l1020">            <span class="n">filename</span> <span class="o">=</span> <span class="bp">None</span></span><a href="#l1020"></a>
<span id="l1021">        <span class="k">else</span><span class="p">:</span></span><a href="#l1021"></a>
<span id="l1022">            <span class="n">filename</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">module</span><span class="p">,</span> <span class="s">&#39;__file__&#39;</span><span class="p">,</span> <span class="n">module</span><span class="o">.</span><span class="n">__name__</span><span class="p">)</span></span><a href="#l1022"></a>
<span id="l1023">            <span class="k">if</span> <span class="n">filename</span><span class="p">[</span><span class="o">-</span><span class="mi">4</span><span class="p">:]</span> <span class="ow">in</span> <span class="p">(</span><span class="s">&quot;.pyc&quot;</span><span class="p">,</span> <span class="s">&quot;.pyo&quot;</span><span class="p">):</span></span><a href="#l1023"></a>
<span id="l1024">                <span class="n">filename</span> <span class="o">=</span> <span class="n">filename</span><span class="p">[:</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span></span><a href="#l1024"></a>
<span id="l1025">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser</span><span class="o">.</span><span class="n">get_doctest</span><span class="p">(</span><span class="n">docstring</span><span class="p">,</span> <span class="n">globs</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span></span><a href="#l1025"></a>
<span id="l1026">                                        <span class="n">filename</span><span class="p">,</span> <span class="n">lineno</span><span class="p">)</span></span><a href="#l1026"></a>
<span id="l1027"></span><a href="#l1027"></a>
<span id="l1028">    <span class="k">def</span> <span class="nf">_find_lineno</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">,</span> <span class="n">source_lines</span><span class="p">):</span></span><a href="#l1028"></a>
<span id="l1029">        <span class="sd">&quot;&quot;&quot;</span></span><a href="#l1029"></a>
<span id="l1030"><span class="sd">        Return a line number of the given object&#39;s docstring.  Note:</span></span><a href="#l1030"></a>
<span id="l1031"><span class="sd">        this method assumes that the object has a docstring.</span></span><a href="#l1031"></a>
<span id="l1032"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l1032"></a>
<span id="l1033">        <span class="n">lineno</span> <span class="o">=</span> <span class="bp">None</span></span><a href="#l1033"></a>
<span id="l1034"></span><a href="#l1034"></a>
<span id="l1035">        <span class="c"># Find the line number for modules.</span></span><a href="#l1035"></a>
<span id="l1036">        <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">ismodule</span><span class="p">(</span><span class="n">obj</span><span class="p">):</span></span><a href="#l1036"></a>
<span id="l1037">            <span class="n">lineno</span> <span class="o">=</span> <span class="mi">0</span></span><a href="#l1037"></a>
<span id="l1038"></span><a href="#l1038"></a>
<span id="l1039">        <span class="c"># Find the line number for classes.</span></span><a href="#l1039"></a>
<span id="l1040">        <span class="c"># Note: this could be fooled if a class is defined multiple</span></span><a href="#l1040"></a>
<span id="l1041">        <span class="c"># times in a single file.</span></span><a href="#l1041"></a>
<span id="l1042">        <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">isclass</span><span class="p">(</span><span class="n">obj</span><span class="p">):</span></span><a href="#l1042"></a>
<span id="l1043">            <span class="k">if</span> <span class="n">source_lines</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1043"></a>
<span id="l1044">                <span class="k">return</span> <span class="bp">None</span></span><a href="#l1044"></a>
<span id="l1045">            <span class="n">pat</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="s">r&#39;^\s*class\s*</span><span class="si">%s</span><span class="s">\b&#39;</span> <span class="o">%</span></span><a href="#l1045"></a>
<span id="l1046">                             <span class="nb">getattr</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="s">&#39;__name__&#39;</span><span class="p">,</span> <span class="s">&#39;-&#39;</span><span class="p">))</span></span><a href="#l1046"></a>
<span id="l1047">            <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">line</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">source_lines</span><span class="p">):</span></span><a href="#l1047"></a>
<span id="l1048">                <span class="k">if</span> <span class="n">pat</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="n">line</span><span class="p">):</span></span><a href="#l1048"></a>
<span id="l1049">                    <span class="n">lineno</span> <span class="o">=</span> <span class="n">i</span></span><a href="#l1049"></a>
<span id="l1050">                    <span class="k">break</span></span><a href="#l1050"></a>
<span id="l1051"></span><a href="#l1051"></a>
<span id="l1052">        <span class="c"># Find the line number for functions &amp; methods.</span></span><a href="#l1052"></a>
<span id="l1053">        <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">ismethod</span><span class="p">(</span><span class="n">obj</span><span class="p">):</span> <span class="n">obj</span> <span class="o">=</span> <span class="n">obj</span><span class="o">.</span><span class="n">im_func</span></span><a href="#l1053"></a>
<span id="l1054">        <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">isfunction</span><span class="p">(</span><span class="n">obj</span><span class="p">):</span> <span class="n">obj</span> <span class="o">=</span> <span class="n">obj</span><span class="o">.</span><span class="n">func_code</span></span><a href="#l1054"></a>
<span id="l1055">        <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">istraceback</span><span class="p">(</span><span class="n">obj</span><span class="p">):</span> <span class="n">obj</span> <span class="o">=</span> <span class="n">obj</span><span class="o">.</span><span class="n">tb_frame</span></span><a href="#l1055"></a>
<span id="l1056">        <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">isframe</span><span class="p">(</span><span class="n">obj</span><span class="p">):</span> <span class="n">obj</span> <span class="o">=</span> <span class="n">obj</span><span class="o">.</span><span class="n">f_code</span></span><a href="#l1056"></a>
<span id="l1057">        <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">iscode</span><span class="p">(</span><span class="n">obj</span><span class="p">):</span></span><a href="#l1057"></a>
<span id="l1058">            <span class="n">lineno</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="s">&#39;co_firstlineno&#39;</span><span class="p">,</span> <span class="bp">None</span><span class="p">)</span><span class="o">-</span><span class="mi">1</span></span><a href="#l1058"></a>
<span id="l1059"></span><a href="#l1059"></a>
<span id="l1060">        <span class="c"># Find the line number where the docstring starts.  Assume</span></span><a href="#l1060"></a>
<span id="l1061">        <span class="c"># that it&#39;s the first line that begins with a quote mark.</span></span><a href="#l1061"></a>
<span id="l1062">        <span class="c"># Note: this could be fooled by a multiline function</span></span><a href="#l1062"></a>
<span id="l1063">        <span class="c"># signature, where a continuation line begins with a quote</span></span><a href="#l1063"></a>
<span id="l1064">        <span class="c"># mark.</span></span><a href="#l1064"></a>
<span id="l1065">        <span class="k">if</span> <span class="n">lineno</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1065"></a>
<span id="l1066">            <span class="k">if</span> <span class="n">source_lines</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1066"></a>
<span id="l1067">                <span class="k">return</span> <span class="n">lineno</span><span class="o">+</span><span class="mi">1</span></span><a href="#l1067"></a>
<span id="l1068">            <span class="n">pat</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="s">&#39;(^|.*:)\s*\w*(&quot;|</span><span class="se">\&#39;</span><span class="s">)&#39;</span><span class="p">)</span></span><a href="#l1068"></a>
<span id="l1069">            <span class="k">for</span> <span class="n">lineno</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">lineno</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">source_lines</span><span class="p">)):</span></span><a href="#l1069"></a>
<span id="l1070">                <span class="k">if</span> <span class="n">pat</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="n">source_lines</span><span class="p">[</span><span class="n">lineno</span><span class="p">]):</span></span><a href="#l1070"></a>
<span id="l1071">                    <span class="k">return</span> <span class="n">lineno</span></span><a href="#l1071"></a>
<span id="l1072"></span><a href="#l1072"></a>
<span id="l1073">        <span class="c"># We couldn&#39;t find the line number.</span></span><a href="#l1073"></a>
<span id="l1074">        <span class="k">return</span> <span class="bp">None</span></span><a href="#l1074"></a>
<span id="l1075"></span><a href="#l1075"></a>
<span id="l1076"><span class="c">######################################################################</span></span><a href="#l1076"></a>
<span id="l1077"><span class="c">## 5. DocTest Runner</span></span><a href="#l1077"></a>
<span id="l1078"><span class="c">######################################################################</span></span><a href="#l1078"></a>
<span id="l1079"></span><a href="#l1079"></a>
<span id="l1080"><span class="k">class</span> <span class="nc">DocTestRunner</span><span class="p">:</span></span><a href="#l1080"></a>
<span id="l1081">    <span class="sd">&quot;&quot;&quot;</span></span><a href="#l1081"></a>
<span id="l1082"><span class="sd">    A class used to run DocTest test cases, and accumulate statistics.</span></span><a href="#l1082"></a>
<span id="l1083"><span class="sd">    The `run` method is used to process a single DocTest case.  It</span></span><a href="#l1083"></a>
<span id="l1084"><span class="sd">    returns a tuple `(f, t)`, where `t` is the number of test cases</span></span><a href="#l1084"></a>
<span id="l1085"><span class="sd">    tried, and `f` is the number of test cases that failed.</span></span><a href="#l1085"></a>
<span id="l1086"></span><a href="#l1086"></a>
<span id="l1087"><span class="sd">        &gt;&gt;&gt; tests = DocTestFinder().find(_TestClass)</span></span><a href="#l1087"></a>
<span id="l1088"><span class="sd">        &gt;&gt;&gt; runner = DocTestRunner(verbose=False)</span></span><a href="#l1088"></a>
<span id="l1089"><span class="sd">        &gt;&gt;&gt; tests.sort(key = lambda test: test.name)</span></span><a href="#l1089"></a>
<span id="l1090"><span class="sd">        &gt;&gt;&gt; for test in tests:</span></span><a href="#l1090"></a>
<span id="l1091"><span class="sd">        ...     print test.name, &#39;-&gt;&#39;, runner.run(test)</span></span><a href="#l1091"></a>
<span id="l1092"><span class="sd">        _TestClass -&gt; TestResults(failed=0, attempted=2)</span></span><a href="#l1092"></a>
<span id="l1093"><span class="sd">        _TestClass.__init__ -&gt; TestResults(failed=0, attempted=2)</span></span><a href="#l1093"></a>
<span id="l1094"><span class="sd">        _TestClass.get -&gt; TestResults(failed=0, attempted=2)</span></span><a href="#l1094"></a>
<span id="l1095"><span class="sd">        _TestClass.square -&gt; TestResults(failed=0, attempted=1)</span></span><a href="#l1095"></a>
<span id="l1096"></span><a href="#l1096"></a>
<span id="l1097"><span class="sd">    The `summarize` method prints a summary of all the test cases that</span></span><a href="#l1097"></a>
<span id="l1098"><span class="sd">    have been run by the runner, and returns an aggregated `(f, t)`</span></span><a href="#l1098"></a>
<span id="l1099"><span class="sd">    tuple:</span></span><a href="#l1099"></a>
<span id="l1100"></span><a href="#l1100"></a>
<span id="l1101"><span class="sd">        &gt;&gt;&gt; runner.summarize(verbose=1)</span></span><a href="#l1101"></a>
<span id="l1102"><span class="sd">        4 items passed all tests:</span></span><a href="#l1102"></a>
<span id="l1103"><span class="sd">           2 tests in _TestClass</span></span><a href="#l1103"></a>
<span id="l1104"><span class="sd">           2 tests in _TestClass.__init__</span></span><a href="#l1104"></a>
<span id="l1105"><span class="sd">           2 tests in _TestClass.get</span></span><a href="#l1105"></a>
<span id="l1106"><span class="sd">           1 tests in _TestClass.square</span></span><a href="#l1106"></a>
<span id="l1107"><span class="sd">        7 tests in 4 items.</span></span><a href="#l1107"></a>
<span id="l1108"><span class="sd">        7 passed and 0 failed.</span></span><a href="#l1108"></a>
<span id="l1109"><span class="sd">        Test passed.</span></span><a href="#l1109"></a>
<span id="l1110"><span class="sd">        TestResults(failed=0, attempted=7)</span></span><a href="#l1110"></a>
<span id="l1111"></span><a href="#l1111"></a>
<span id="l1112"><span class="sd">    The aggregated number of tried examples and failed examples is</span></span><a href="#l1112"></a>
<span id="l1113"><span class="sd">    also available via the `tries` and `failures` attributes:</span></span><a href="#l1113"></a>
<span id="l1114"></span><a href="#l1114"></a>
<span id="l1115"><span class="sd">        &gt;&gt;&gt; runner.tries</span></span><a href="#l1115"></a>
<span id="l1116"><span class="sd">        7</span></span><a href="#l1116"></a>
<span id="l1117"><span class="sd">        &gt;&gt;&gt; runner.failures</span></span><a href="#l1117"></a>
<span id="l1118"><span class="sd">        0</span></span><a href="#l1118"></a>
<span id="l1119"></span><a href="#l1119"></a>
<span id="l1120"><span class="sd">    The comparison between expected outputs and actual outputs is done</span></span><a href="#l1120"></a>
<span id="l1121"><span class="sd">    by an `OutputChecker`.  This comparison may be customized with a</span></span><a href="#l1121"></a>
<span id="l1122"><span class="sd">    number of option flags; see the documentation for `testmod` for</span></span><a href="#l1122"></a>
<span id="l1123"><span class="sd">    more information.  If the option flags are insufficient, then the</span></span><a href="#l1123"></a>
<span id="l1124"><span class="sd">    comparison may also be customized by passing a subclass of</span></span><a href="#l1124"></a>
<span id="l1125"><span class="sd">    `OutputChecker` to the constructor.</span></span><a href="#l1125"></a>
<span id="l1126"></span><a href="#l1126"></a>
<span id="l1127"><span class="sd">    The test runner&#39;s display output can be controlled in two ways.</span></span><a href="#l1127"></a>
<span id="l1128"><span class="sd">    First, an output function (`out) can be passed to</span></span><a href="#l1128"></a>
<span id="l1129"><span class="sd">    `TestRunner.run`; this function will be called with strings that</span></span><a href="#l1129"></a>
<span id="l1130"><span class="sd">    should be displayed.  It defaults to `sys.stdout.write`.  If</span></span><a href="#l1130"></a>
<span id="l1131"><span class="sd">    capturing the output is not sufficient, then the display output</span></span><a href="#l1131"></a>
<span id="l1132"><span class="sd">    can be also customized by subclassing DocTestRunner, and</span></span><a href="#l1132"></a>
<span id="l1133"><span class="sd">    overriding the methods `report_start`, `report_success`,</span></span><a href="#l1133"></a>
<span id="l1134"><span class="sd">    `report_unexpected_exception`, and `report_failure`.</span></span><a href="#l1134"></a>
<span id="l1135"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l1135"></a>
<span id="l1136">    <span class="c"># This divider string is used to separate failure messages, and to</span></span><a href="#l1136"></a>
<span id="l1137">    <span class="c"># separate sections of the summary.</span></span><a href="#l1137"></a>
<span id="l1138">    <span class="n">DIVIDER</span> <span class="o">=</span> <span class="s">&quot;*&quot;</span> <span class="o">*</span> <span class="mi">70</span></span><a href="#l1138"></a>
<span id="l1139"></span><a href="#l1139"></a>
<span id="l1140">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">checker</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">verbose</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">optionflags</span><span class="o">=</span><span class="mi">0</span><span class="p">):</span></span><a href="#l1140"></a>
<span id="l1141">        <span class="sd">&quot;&quot;&quot;</span></span><a href="#l1141"></a>
<span id="l1142"><span class="sd">        Create a new test runner.</span></span><a href="#l1142"></a>
<span id="l1143"></span><a href="#l1143"></a>
<span id="l1144"><span class="sd">        Optional keyword arg `checker` is the `OutputChecker` that</span></span><a href="#l1144"></a>
<span id="l1145"><span class="sd">        should be used to compare the expected outputs and actual</span></span><a href="#l1145"></a>
<span id="l1146"><span class="sd">        outputs of doctest examples.</span></span><a href="#l1146"></a>
<span id="l1147"></span><a href="#l1147"></a>
<span id="l1148"><span class="sd">        Optional keyword arg &#39;verbose&#39; prints lots of stuff if true,</span></span><a href="#l1148"></a>
<span id="l1149"><span class="sd">        only failures if false; by default, it&#39;s true iff &#39;-v&#39; is in</span></span><a href="#l1149"></a>
<span id="l1150"><span class="sd">        sys.argv.</span></span><a href="#l1150"></a>
<span id="l1151"></span><a href="#l1151"></a>
<span id="l1152"><span class="sd">        Optional argument `optionflags` can be used to control how the</span></span><a href="#l1152"></a>
<span id="l1153"><span class="sd">        test runner compares expected output to actual output, and how</span></span><a href="#l1153"></a>
<span id="l1154"><span class="sd">        it displays failures.  See the documentation for `testmod` for</span></span><a href="#l1154"></a>
<span id="l1155"><span class="sd">        more information.</span></span><a href="#l1155"></a>
<span id="l1156"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l1156"></a>
<span id="l1157">        <span class="bp">self</span><span class="o">.</span><span class="n">_checker</span> <span class="o">=</span> <span class="n">checker</span> <span class="ow">or</span> <span class="n">OutputChecker</span><span class="p">()</span></span><a href="#l1157"></a>
<span id="l1158">        <span class="k">if</span> <span class="n">verbose</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1158"></a>
<span id="l1159">            <span class="n">verbose</span> <span class="o">=</span> <span class="s">&#39;-v&#39;</span> <span class="ow">in</span> <span class="n">sys</span><span class="o">.</span><span class="n">argv</span></span><a href="#l1159"></a>
<span id="l1160">        <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span> <span class="o">=</span> <span class="n">verbose</span></span><a href="#l1160"></a>
<span id="l1161">        <span class="bp">self</span><span class="o">.</span><span class="n">optionflags</span> <span class="o">=</span> <span class="n">optionflags</span></span><a href="#l1161"></a>
<span id="l1162">        <span class="bp">self</span><span class="o">.</span><span class="n">original_optionflags</span> <span class="o">=</span> <span class="n">optionflags</span></span><a href="#l1162"></a>
<span id="l1163"></span><a href="#l1163"></a>
<span id="l1164">        <span class="c"># Keep track of the examples we&#39;ve run.</span></span><a href="#l1164"></a>
<span id="l1165">        <span class="bp">self</span><span class="o">.</span><span class="n">tries</span> <span class="o">=</span> <span class="mi">0</span></span><a href="#l1165"></a>
<span id="l1166">        <span class="bp">self</span><span class="o">.</span><span class="n">failures</span> <span class="o">=</span> <span class="mi">0</span></span><a href="#l1166"></a>
<span id="l1167">        <span class="bp">self</span><span class="o">.</span><span class="n">_name2ft</span> <span class="o">=</span> <span class="p">{}</span></span><a href="#l1167"></a>
<span id="l1168"></span><a href="#l1168"></a>
<span id="l1169">        <span class="c"># Create a fake output target for capturing doctest output.</span></span><a href="#l1169"></a>
<span id="l1170">        <span class="bp">self</span><span class="o">.</span><span class="n">_fakeout</span> <span class="o">=</span> <span class="n">_SpoofOut</span><span class="p">()</span></span><a href="#l1170"></a>
<span id="l1171"></span><a href="#l1171"></a>
<span id="l1172">    <span class="c">#/////////////////////////////////////////////////////////////////</span></span><a href="#l1172"></a>
<span id="l1173">    <span class="c"># Reporting methods</span></span><a href="#l1173"></a>
<span id="l1174">    <span class="c">#/////////////////////////////////////////////////////////////////</span></span><a href="#l1174"></a>
<span id="l1175"></span><a href="#l1175"></a>
<span id="l1176">    <span class="k">def</span> <span class="nf">report_start</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">out</span><span class="p">,</span> <span class="n">test</span><span class="p">,</span> <span class="n">example</span><span class="p">):</span></span><a href="#l1176"></a>
<span id="l1177">        <span class="sd">&quot;&quot;&quot;</span></span><a href="#l1177"></a>
<span id="l1178"><span class="sd">        Report that the test runner is about to process the given</span></span><a href="#l1178"></a>
<span id="l1179"><span class="sd">        example.  (Only displays a message if verbose=True)</span></span><a href="#l1179"></a>
<span id="l1180"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l1180"></a>
<span id="l1181">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span></span><a href="#l1181"></a>
<span id="l1182">            <span class="k">if</span> <span class="n">example</span><span class="o">.</span><span class="n">want</span><span class="p">:</span></span><a href="#l1182"></a>
<span id="l1183">                <span class="n">out</span><span class="p">(</span><span class="s">&#39;Trying:</span><span class="se">\n</span><span class="s">&#39;</span> <span class="o">+</span> <span class="n">_indent</span><span class="p">(</span><span class="n">example</span><span class="o">.</span><span class="n">source</span><span class="p">)</span> <span class="o">+</span></span><a href="#l1183"></a>
<span id="l1184">                    <span class="s">&#39;Expecting:</span><span class="se">\n</span><span class="s">&#39;</span> <span class="o">+</span> <span class="n">_indent</span><span class="p">(</span><span class="n">example</span><span class="o">.</span><span class="n">want</span><span class="p">))</span></span><a href="#l1184"></a>
<span id="l1185">            <span class="k">else</span><span class="p">:</span></span><a href="#l1185"></a>
<span id="l1186">                <span class="n">out</span><span class="p">(</span><span class="s">&#39;Trying:</span><span class="se">\n</span><span class="s">&#39;</span> <span class="o">+</span> <span class="n">_indent</span><span class="p">(</span><span class="n">example</span><span class="o">.</span><span class="n">source</span><span class="p">)</span> <span class="o">+</span></span><a href="#l1186"></a>
<span id="l1187">                    <span class="s">&#39;Expecting nothing</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span></span><a href="#l1187"></a>
<span id="l1188"></span><a href="#l1188"></a>
<span id="l1189">    <span class="k">def</span> <span class="nf">report_success</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">out</span><span class="p">,</span> <span class="n">test</span><span class="p">,</span> <span class="n">example</span><span class="p">,</span> <span class="n">got</span><span class="p">):</span></span><a href="#l1189"></a>
<span id="l1190">        <span class="sd">&quot;&quot;&quot;</span></span><a href="#l1190"></a>
<span id="l1191"><span class="sd">        Report that the given example ran successfully.  (Only</span></span><a href="#l1191"></a>
<span id="l1192"><span class="sd">        displays a message if verbose=True)</span></span><a href="#l1192"></a>
<span id="l1193"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l1193"></a>
<span id="l1194">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">:</span></span><a href="#l1194"></a>
<span id="l1195">            <span class="n">out</span><span class="p">(</span><span class="s">&quot;ok</span><span class="se">\n</span><span class="s">&quot;</span><span class="p">)</span></span><a href="#l1195"></a>
<span id="l1196"></span><a href="#l1196"></a>
<span id="l1197">    <span class="k">def</span> <span class="nf">report_failure</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">out</span><span class="p">,</span> <span class="n">test</span><span class="p">,</span> <span class="n">example</span><span class="p">,</span> <span class="n">got</span><span class="p">):</span></span><a href="#l1197"></a>
<span id="l1198">        <span class="sd">&quot;&quot;&quot;</span></span><a href="#l1198"></a>
<span id="l1199"><span class="sd">        Report that the given example failed.</span></span><a href="#l1199"></a>
<span id="l1200"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l1200"></a>
<span id="l1201">        <span class="n">out</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_failure_header</span><span class="p">(</span><span class="n">test</span><span class="p">,</span> <span class="n">example</span><span class="p">)</span> <span class="o">+</span></span><a href="#l1201"></a>
<span id="l1202">            <span class="bp">self</span><span class="o">.</span><span class="n">_checker</span><span class="o">.</span><span class="n">output_difference</span><span class="p">(</span><span class="n">example</span><span class="p">,</span> <span class="n">got</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">optionflags</span><span class="p">))</span></span><a href="#l1202"></a>
<span id="l1203"></span><a href="#l1203"></a>
<span id="l1204">    <span class="k">def</span> <span class="nf">report_unexpected_exception</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">out</span><span class="p">,</span> <span class="n">test</span><span class="p">,</span> <span class="n">example</span><span class="p">,</span> <span class="n">exc_info</span><span class="p">):</span></span><a href="#l1204"></a>
<span id="l1205">        <span class="sd">&quot;&quot;&quot;</span></span><a href="#l1205"></a>
<span id="l1206"><span class="sd">        Report that the given example raised an unexpected exception.</span></span><a href="#l1206"></a>
<span id="l1207"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l1207"></a>
<span id="l1208">        <span class="n">out</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_failure_header</span><span class="p">(</span><span class="n">test</span><span class="p">,</span> <span class="n">example</span><span class="p">)</span> <span class="o">+</span></span><a href="#l1208"></a>
<span id="l1209">            <span class="s">&#39;Exception raised:</span><span class="se">\n</span><span class="s">&#39;</span> <span class="o">+</span> <span class="n">_indent</span><span class="p">(</span><span class="n">_exception_traceback</span><span class="p">(</span><span class="n">exc_info</span><span class="p">)))</span></span><a href="#l1209"></a>
<span id="l1210"></span><a href="#l1210"></a>
<span id="l1211">    <span class="k">def</span> <span class="nf">_failure_header</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">test</span><span class="p">,</span> <span class="n">example</span><span class="p">):</span></span><a href="#l1211"></a>
<span id="l1212">        <span class="n">out</span> <span class="o">=</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">DIVIDER</span><span class="p">]</span></span><a href="#l1212"></a>
<span id="l1213">        <span class="k">if</span> <span class="n">test</span><span class="o">.</span><span class="n">filename</span><span class="p">:</span></span><a href="#l1213"></a>
<span id="l1214">            <span class="k">if</span> <span class="n">test</span><span class="o">.</span><span class="n">lineno</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span> <span class="ow">and</span> <span class="n">example</span><span class="o">.</span><span class="n">lineno</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1214"></a>
<span id="l1215">                <span class="n">lineno</span> <span class="o">=</span> <span class="n">test</span><span class="o">.</span><span class="n">lineno</span> <span class="o">+</span> <span class="n">example</span><span class="o">.</span><span class="n">lineno</span> <span class="o">+</span> <span class="mi">1</span></span><a href="#l1215"></a>
<span id="l1216">            <span class="k">else</span><span class="p">:</span></span><a href="#l1216"></a>
<span id="l1217">                <span class="n">lineno</span> <span class="o">=</span> <span class="s">&#39;?&#39;</span></span><a href="#l1217"></a>
<span id="l1218">            <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s">&#39;File &quot;</span><span class="si">%s</span><span class="s">&quot;, line </span><span class="si">%s</span><span class="s">, in </span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span></span><a href="#l1218"></a>
<span id="l1219">                       <span class="p">(</span><span class="n">test</span><span class="o">.</span><span class="n">filename</span><span class="p">,</span> <span class="n">lineno</span><span class="p">,</span> <span class="n">test</span><span class="o">.</span><span class="n">name</span><span class="p">))</span></span><a href="#l1219"></a>
<span id="l1220">        <span class="k">else</span><span class="p">:</span></span><a href="#l1220"></a>
<span id="l1221">            <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s">&#39;Line </span><span class="si">%s</span><span class="s">, in </span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">example</span><span class="o">.</span><span class="n">lineno</span><span class="o">+</span><span class="mi">1</span><span class="p">,</span> <span class="n">test</span><span class="o">.</span><span class="n">name</span><span class="p">))</span></span><a href="#l1221"></a>
<span id="l1222">        <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s">&#39;Failed example:&#39;</span><span class="p">)</span></span><a href="#l1222"></a>
<span id="l1223">        <span class="n">source</span> <span class="o">=</span> <span class="n">example</span><span class="o">.</span><span class="n">source</span></span><a href="#l1223"></a>
<span id="l1224">        <span class="n">out</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">_indent</span><span class="p">(</span><span class="n">source</span><span class="p">))</span></span><a href="#l1224"></a>
<span id="l1225">        <span class="k">return</span> <span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">out</span><span class="p">)</span></span><a href="#l1225"></a>
<span id="l1226"></span><a href="#l1226"></a>
<span id="l1227">    <span class="c">#/////////////////////////////////////////////////////////////////</span></span><a href="#l1227"></a>
<span id="l1228">    <span class="c"># DocTest Running</span></span><a href="#l1228"></a>
<span id="l1229">    <span class="c">#/////////////////////////////////////////////////////////////////</span></span><a href="#l1229"></a>
<span id="l1230"></span><a href="#l1230"></a>
<span id="l1231">    <span class="k">def</span> <span class="nf">__run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">test</span><span class="p">,</span> <span class="n">compileflags</span><span class="p">,</span> <span class="n">out</span><span class="p">):</span></span><a href="#l1231"></a>
<span id="l1232">        <span class="sd">&quot;&quot;&quot;</span></span><a href="#l1232"></a>
<span id="l1233"><span class="sd">        Run the examples in `test`.  Write the outcome of each example</span></span><a href="#l1233"></a>
<span id="l1234"><span class="sd">        with one of the `DocTestRunner.report_*` methods, using the</span></span><a href="#l1234"></a>
<span id="l1235"><span class="sd">        writer function `out`.  `compileflags` is the set of compiler</span></span><a href="#l1235"></a>
<span id="l1236"><span class="sd">        flags that should be used to execute examples.  Return a tuple</span></span><a href="#l1236"></a>
<span id="l1237"><span class="sd">        `(f, t)`, where `t` is the number of examples tried, and `f`</span></span><a href="#l1237"></a>
<span id="l1238"><span class="sd">        is the number of examples that failed.  The examples are run</span></span><a href="#l1238"></a>
<span id="l1239"><span class="sd">        in the namespace `test.globs`.</span></span><a href="#l1239"></a>
<span id="l1240"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l1240"></a>
<span id="l1241">        <span class="c"># Keep track of the number of failures and tries.</span></span><a href="#l1241"></a>
<span id="l1242">        <span class="n">failures</span> <span class="o">=</span> <span class="n">tries</span> <span class="o">=</span> <span class="mi">0</span></span><a href="#l1242"></a>
<span id="l1243"></span><a href="#l1243"></a>
<span id="l1244">        <span class="c"># Save the option flags (since option directives can be used</span></span><a href="#l1244"></a>
<span id="l1245">        <span class="c"># to modify them).</span></span><a href="#l1245"></a>
<span id="l1246">        <span class="n">original_optionflags</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">optionflags</span></span><a href="#l1246"></a>
<span id="l1247"></span><a href="#l1247"></a>
<span id="l1248">        <span class="n">SUCCESS</span><span class="p">,</span> <span class="n">FAILURE</span><span class="p">,</span> <span class="n">BOOM</span> <span class="o">=</span> <span class="nb">range</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span> <span class="c"># `outcome` state</span></span><a href="#l1248"></a>
<span id="l1249"></span><a href="#l1249"></a>
<span id="l1250">        <span class="n">check</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_checker</span><span class="o">.</span><span class="n">check_output</span></span><a href="#l1250"></a>
<span id="l1251"></span><a href="#l1251"></a>
<span id="l1252">        <span class="c"># Process each example.</span></span><a href="#l1252"></a>
<span id="l1253">        <span class="k">for</span> <span class="n">examplenum</span><span class="p">,</span> <span class="n">example</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">test</span><span class="o">.</span><span class="n">examples</span><span class="p">):</span></span><a href="#l1253"></a>
<span id="l1254"></span><a href="#l1254"></a>
<span id="l1255">            <span class="c"># If REPORT_ONLY_FIRST_FAILURE is set, then suppress</span></span><a href="#l1255"></a>
<span id="l1256">            <span class="c"># reporting after the first failure.</span></span><a href="#l1256"></a>
<span id="l1257">            <span class="n">quiet</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">optionflags</span> <span class="o">&amp;</span> <span class="n">REPORT_ONLY_FIRST_FAILURE</span> <span class="ow">and</span></span><a href="#l1257"></a>
<span id="l1258">                     <span class="n">failures</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">)</span></span><a href="#l1258"></a>
<span id="l1259"></span><a href="#l1259"></a>
<span id="l1260">            <span class="c"># Merge in the example&#39;s options.</span></span><a href="#l1260"></a>
<span id="l1261">            <span class="bp">self</span><span class="o">.</span><span class="n">optionflags</span> <span class="o">=</span> <span class="n">original_optionflags</span></span><a href="#l1261"></a>
<span id="l1262">            <span class="k">if</span> <span class="n">example</span><span class="o">.</span><span class="n">options</span><span class="p">:</span></span><a href="#l1262"></a>
<span id="l1263">                <span class="k">for</span> <span class="p">(</span><span class="n">optionflag</span><span class="p">,</span> <span class="n">val</span><span class="p">)</span> <span class="ow">in</span> <span class="n">example</span><span class="o">.</span><span class="n">options</span><span class="o">.</span><span class="n">items</span><span class="p">():</span></span><a href="#l1263"></a>
<span id="l1264">                    <span class="k">if</span> <span class="n">val</span><span class="p">:</span></span><a href="#l1264"></a>
<span id="l1265">                        <span class="bp">self</span><span class="o">.</span><span class="n">optionflags</span> <span class="o">|=</span> <span class="n">optionflag</span></span><a href="#l1265"></a>
<span id="l1266">                    <span class="k">else</span><span class="p">:</span></span><a href="#l1266"></a>
<span id="l1267">                        <span class="bp">self</span><span class="o">.</span><span class="n">optionflags</span> <span class="o">&amp;=</span> <span class="o">~</span><span class="n">optionflag</span></span><a href="#l1267"></a>
<span id="l1268"></span><a href="#l1268"></a>
<span id="l1269">            <span class="c"># If &#39;SKIP&#39; is set, then skip this example.</span></span><a href="#l1269"></a>
<span id="l1270">            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">optionflags</span> <span class="o">&amp;</span> <span class="n">SKIP</span><span class="p">:</span></span><a href="#l1270"></a>
<span id="l1271">                <span class="k">continue</span></span><a href="#l1271"></a>
<span id="l1272"></span><a href="#l1272"></a>
<span id="l1273">            <span class="c"># Record that we started this example.</span></span><a href="#l1273"></a>
<span id="l1274">            <span class="n">tries</span> <span class="o">+=</span> <span class="mi">1</span></span><a href="#l1274"></a>
<span id="l1275">            <span class="k">if</span> <span class="ow">not</span> <span class="n">quiet</span><span class="p">:</span></span><a href="#l1275"></a>
<span id="l1276">                <span class="bp">self</span><span class="o">.</span><span class="n">report_start</span><span class="p">(</span><span class="n">out</span><span class="p">,</span> <span class="n">test</span><span class="p">,</span> <span class="n">example</span><span class="p">)</span></span><a href="#l1276"></a>
<span id="l1277"></span><a href="#l1277"></a>
<span id="l1278">            <span class="c"># Use a special filename for compile(), so we can retrieve</span></span><a href="#l1278"></a>
<span id="l1279">            <span class="c"># the source code during interactive debugging (see</span></span><a href="#l1279"></a>
<span id="l1280">            <span class="c"># __patched_linecache_getlines).</span></span><a href="#l1280"></a>
<span id="l1281">            <span class="n">filename</span> <span class="o">=</span> <span class="s">&#39;&lt;doctest </span><span class="si">%s</span><span class="s">[</span><span class="si">%d</span><span class="s">]&gt;&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">test</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="n">examplenum</span><span class="p">)</span></span><a href="#l1281"></a>
<span id="l1282"></span><a href="#l1282"></a>
<span id="l1283">            <span class="c"># Run the example in the given context (globs), and record</span></span><a href="#l1283"></a>
<span id="l1284">            <span class="c"># any exception that gets raised.  (But don&#39;t intercept</span></span><a href="#l1284"></a>
<span id="l1285">            <span class="c"># keyboard interrupts.)</span></span><a href="#l1285"></a>
<span id="l1286">            <span class="k">try</span><span class="p">:</span></span><a href="#l1286"></a>
<span id="l1287">                <span class="c"># Don&#39;t blink!  This is where the user&#39;s code gets run.</span></span><a href="#l1287"></a>
<span id="l1288">                <span class="k">exec</span> <span class="nb">compile</span><span class="p">(</span><span class="n">example</span><span class="o">.</span><span class="n">source</span><span class="p">,</span> <span class="n">filename</span><span class="p">,</span> <span class="s">&quot;single&quot;</span><span class="p">,</span></span><a href="#l1288"></a>
<span id="l1289">                             <span class="n">compileflags</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span> <span class="ow">in</span> <span class="n">test</span><span class="o">.</span><span class="n">globs</span></span><a href="#l1289"></a>
<span id="l1290">                <span class="bp">self</span><span class="o">.</span><span class="n">debugger</span><span class="o">.</span><span class="n">set_continue</span><span class="p">()</span> <span class="c"># ==== Example Finished ====</span></span><a href="#l1290"></a>
<span id="l1291">                <span class="n">exception</span> <span class="o">=</span> <span class="bp">None</span></span><a href="#l1291"></a>
<span id="l1292">            <span class="k">except</span> <span class="ne">KeyboardInterrupt</span><span class="p">:</span></span><a href="#l1292"></a>
<span id="l1293">                <span class="k">raise</span></span><a href="#l1293"></a>
<span id="l1294">            <span class="k">except</span><span class="p">:</span></span><a href="#l1294"></a>
<span id="l1295">                <span class="n">exception</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">exc_info</span><span class="p">()</span></span><a href="#l1295"></a>
<span id="l1296">                <span class="bp">self</span><span class="o">.</span><span class="n">debugger</span><span class="o">.</span><span class="n">set_continue</span><span class="p">()</span> <span class="c"># ==== Example Finished ====</span></span><a href="#l1296"></a>
<span id="l1297"></span><a href="#l1297"></a>
<span id="l1298">            <span class="n">got</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_fakeout</span><span class="o">.</span><span class="n">getvalue</span><span class="p">()</span>  <span class="c"># the actual output</span></span><a href="#l1298"></a>
<span id="l1299">            <span class="bp">self</span><span class="o">.</span><span class="n">_fakeout</span><span class="o">.</span><span class="n">truncate</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span></span><a href="#l1299"></a>
<span id="l1300">            <span class="n">outcome</span> <span class="o">=</span> <span class="n">FAILURE</span>   <span class="c"># guilty until proved innocent or insane</span></span><a href="#l1300"></a>
<span id="l1301"></span><a href="#l1301"></a>
<span id="l1302">            <span class="c"># If the example executed without raising any exceptions,</span></span><a href="#l1302"></a>
<span id="l1303">            <span class="c"># verify its output.</span></span><a href="#l1303"></a>
<span id="l1304">            <span class="k">if</span> <span class="n">exception</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1304"></a>
<span id="l1305">                <span class="k">if</span> <span class="n">check</span><span class="p">(</span><span class="n">example</span><span class="o">.</span><span class="n">want</span><span class="p">,</span> <span class="n">got</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">optionflags</span><span class="p">):</span></span><a href="#l1305"></a>
<span id="l1306">                    <span class="n">outcome</span> <span class="o">=</span> <span class="n">SUCCESS</span></span><a href="#l1306"></a>
<span id="l1307"></span><a href="#l1307"></a>
<span id="l1308">            <span class="c"># The example raised an exception:  check if it was expected.</span></span><a href="#l1308"></a>
<span id="l1309">            <span class="k">else</span><span class="p">:</span></span><a href="#l1309"></a>
<span id="l1310">                <span class="n">exc_info</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">exc_info</span><span class="p">()</span></span><a href="#l1310"></a>
<span id="l1311">                <span class="n">exc_msg</span> <span class="o">=</span> <span class="n">traceback</span><span class="o">.</span><span class="n">format_exception_only</span><span class="p">(</span><span class="o">*</span><span class="n">exc_info</span><span class="p">[:</span><span class="mi">2</span><span class="p">])[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span></span><a href="#l1311"></a>
<span id="l1312">                <span class="k">if</span> <span class="ow">not</span> <span class="n">quiet</span><span class="p">:</span></span><a href="#l1312"></a>
<span id="l1313">                    <span class="n">got</span> <span class="o">+=</span> <span class="n">_exception_traceback</span><span class="p">(</span><span class="n">exc_info</span><span class="p">)</span></span><a href="#l1313"></a>
<span id="l1314"></span><a href="#l1314"></a>
<span id="l1315">                <span class="c"># If `example.exc_msg` is None, then we weren&#39;t expecting</span></span><a href="#l1315"></a>
<span id="l1316">                <span class="c"># an exception.</span></span><a href="#l1316"></a>
<span id="l1317">                <span class="k">if</span> <span class="n">example</span><span class="o">.</span><span class="n">exc_msg</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1317"></a>
<span id="l1318">                    <span class="n">outcome</span> <span class="o">=</span> <span class="n">BOOM</span></span><a href="#l1318"></a>
<span id="l1319"></span><a href="#l1319"></a>
<span id="l1320">                <span class="c"># We expected an exception:  see whether it matches.</span></span><a href="#l1320"></a>
<span id="l1321">                <span class="k">elif</span> <span class="n">check</span><span class="p">(</span><span class="n">example</span><span class="o">.</span><span class="n">exc_msg</span><span class="p">,</span> <span class="n">exc_msg</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">optionflags</span><span class="p">):</span></span><a href="#l1321"></a>
<span id="l1322">                    <span class="n">outcome</span> <span class="o">=</span> <span class="n">SUCCESS</span></span><a href="#l1322"></a>
<span id="l1323"></span><a href="#l1323"></a>
<span id="l1324">                <span class="c"># Another chance if they didn&#39;t care about the detail.</span></span><a href="#l1324"></a>
<span id="l1325">                <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">optionflags</span> <span class="o">&amp;</span> <span class="n">IGNORE_EXCEPTION_DETAIL</span><span class="p">:</span></span><a href="#l1325"></a>
<span id="l1326">                    <span class="n">m1</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="s">r&#39;(?:[^:]*\.)?([^:]*:)&#39;</span><span class="p">,</span> <span class="n">example</span><span class="o">.</span><span class="n">exc_msg</span><span class="p">)</span></span><a href="#l1326"></a>
<span id="l1327">                    <span class="n">m2</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="s">r&#39;(?:[^:]*\.)?([^:]*:)&#39;</span><span class="p">,</span> <span class="n">exc_msg</span><span class="p">)</span></span><a href="#l1327"></a>
<span id="l1328">                    <span class="k">if</span> <span class="n">m1</span> <span class="ow">and</span> <span class="n">m2</span> <span class="ow">and</span> <span class="n">check</span><span class="p">(</span><span class="n">m1</span><span class="o">.</span><span class="n">group</span><span class="p">(</span><span class="mi">1</span><span class="p">),</span> <span class="n">m2</span><span class="o">.</span><span class="n">group</span><span class="p">(</span><span class="mi">1</span><span class="p">),</span></span><a href="#l1328"></a>
<span id="l1329">                                           <span class="bp">self</span><span class="o">.</span><span class="n">optionflags</span><span class="p">):</span></span><a href="#l1329"></a>
<span id="l1330">                        <span class="n">outcome</span> <span class="o">=</span> <span class="n">SUCCESS</span></span><a href="#l1330"></a>
<span id="l1331"></span><a href="#l1331"></a>
<span id="l1332">            <span class="c"># Report the outcome.</span></span><a href="#l1332"></a>
<span id="l1333">            <span class="k">if</span> <span class="n">outcome</span> <span class="ow">is</span> <span class="n">SUCCESS</span><span class="p">:</span></span><a href="#l1333"></a>
<span id="l1334">                <span class="k">if</span> <span class="ow">not</span> <span class="n">quiet</span><span class="p">:</span></span><a href="#l1334"></a>
<span id="l1335">                    <span class="bp">self</span><span class="o">.</span><span class="n">report_success</span><span class="p">(</span><span class="n">out</span><span class="p">,</span> <span class="n">test</span><span class="p">,</span> <span class="n">example</span><span class="p">,</span> <span class="n">got</span><span class="p">)</span></span><a href="#l1335"></a>
<span id="l1336">            <span class="k">elif</span> <span class="n">outcome</span> <span class="ow">is</span> <span class="n">FAILURE</span><span class="p">:</span></span><a href="#l1336"></a>
<span id="l1337">                <span class="k">if</span> <span class="ow">not</span> <span class="n">quiet</span><span class="p">:</span></span><a href="#l1337"></a>
<span id="l1338">                    <span class="bp">self</span><span class="o">.</span><span class="n">report_failure</span><span class="p">(</span><span class="n">out</span><span class="p">,</span> <span class="n">test</span><span class="p">,</span> <span class="n">example</span><span class="p">,</span> <span class="n">got</span><span class="p">)</span></span><a href="#l1338"></a>
<span id="l1339">                <span class="n">failures</span> <span class="o">+=</span> <span class="mi">1</span></span><a href="#l1339"></a>
<span id="l1340">            <span class="k">elif</span> <span class="n">outcome</span> <span class="ow">is</span> <span class="n">BOOM</span><span class="p">:</span></span><a href="#l1340"></a>
<span id="l1341">                <span class="k">if</span> <span class="ow">not</span> <span class="n">quiet</span><span class="p">:</span></span><a href="#l1341"></a>
<span id="l1342">                    <span class="bp">self</span><span class="o">.</span><span class="n">report_unexpected_exception</span><span class="p">(</span><span class="n">out</span><span class="p">,</span> <span class="n">test</span><span class="p">,</span> <span class="n">example</span><span class="p">,</span></span><a href="#l1342"></a>
<span id="l1343">                                                     <span class="n">exc_info</span><span class="p">)</span></span><a href="#l1343"></a>
<span id="l1344">                <span class="n">failures</span> <span class="o">+=</span> <span class="mi">1</span></span><a href="#l1344"></a>
<span id="l1345">            <span class="k">else</span><span class="p">:</span></span><a href="#l1345"></a>
<span id="l1346">                <span class="k">assert</span> <span class="bp">False</span><span class="p">,</span> <span class="p">(</span><span class="s">&quot;unknown outcome&quot;</span><span class="p">,</span> <span class="n">outcome</span><span class="p">)</span></span><a href="#l1346"></a>
<span id="l1347"></span><a href="#l1347"></a>
<span id="l1348">        <span class="c"># Restore the option flags (in case they were modified)</span></span><a href="#l1348"></a>
<span id="l1349">        <span class="bp">self</span><span class="o">.</span><span class="n">optionflags</span> <span class="o">=</span> <span class="n">original_optionflags</span></span><a href="#l1349"></a>
<span id="l1350"></span><a href="#l1350"></a>
<span id="l1351">        <span class="c"># Record and return the number of failures and tries.</span></span><a href="#l1351"></a>
<span id="l1352">        <span class="bp">self</span><span class="o">.</span><span class="n">__record_outcome</span><span class="p">(</span><span class="n">test</span><span class="p">,</span> <span class="n">failures</span><span class="p">,</span> <span class="n">tries</span><span class="p">)</span></span><a href="#l1352"></a>
<span id="l1353">        <span class="k">return</span> <span class="n">TestResults</span><span class="p">(</span><span class="n">failures</span><span class="p">,</span> <span class="n">tries</span><span class="p">)</span></span><a href="#l1353"></a>
<span id="l1354"></span><a href="#l1354"></a>
<span id="l1355">    <span class="k">def</span> <span class="nf">__record_outcome</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">test</span><span class="p">,</span> <span class="n">f</span><span class="p">,</span> <span class="n">t</span><span class="p">):</span></span><a href="#l1355"></a>
<span id="l1356">        <span class="sd">&quot;&quot;&quot;</span></span><a href="#l1356"></a>
<span id="l1357"><span class="sd">        Record the fact that the given DocTest (`test`) generated `f`</span></span><a href="#l1357"></a>
<span id="l1358"><span class="sd">        failures out of `t` tried examples.</span></span><a href="#l1358"></a>
<span id="l1359"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l1359"></a>
<span id="l1360">        <span class="n">f2</span><span class="p">,</span> <span class="n">t2</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_name2ft</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">test</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">))</span></span><a href="#l1360"></a>
<span id="l1361">        <span class="bp">self</span><span class="o">.</span><span class="n">_name2ft</span><span class="p">[</span><span class="n">test</span><span class="o">.</span><span class="n">name</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">f</span><span class="o">+</span><span class="n">f2</span><span class="p">,</span> <span class="n">t</span><span class="o">+</span><span class="n">t2</span><span class="p">)</span></span><a href="#l1361"></a>
<span id="l1362">        <span class="bp">self</span><span class="o">.</span><span class="n">failures</span> <span class="o">+=</span> <span class="n">f</span></span><a href="#l1362"></a>
<span id="l1363">        <span class="bp">self</span><span class="o">.</span><span class="n">tries</span> <span class="o">+=</span> <span class="n">t</span></span><a href="#l1363"></a>
<span id="l1364"></span><a href="#l1364"></a>
<span id="l1365">    <span class="n">__LINECACHE_FILENAME_RE</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="s">r&#39;&lt;doctest &#39;</span></span><a href="#l1365"></a>
<span id="l1366">                                         <span class="s">r&#39;(?P&lt;name&gt;.+)&#39;</span></span><a href="#l1366"></a>
<span id="l1367">                                         <span class="s">r&#39;\[(?P&lt;examplenum&gt;\d+)\]&gt;$&#39;</span><span class="p">)</span></span><a href="#l1367"></a>
<span id="l1368">    <span class="k">def</span> <span class="nf">__patched_linecache_getlines</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">filename</span><span class="p">,</span> <span class="n">module_globals</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l1368"></a>
<span id="l1369">        <span class="n">m</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__LINECACHE_FILENAME_RE</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="n">filename</span><span class="p">)</span></span><a href="#l1369"></a>
<span id="l1370">        <span class="k">if</span> <span class="n">m</span> <span class="ow">and</span> <span class="n">m</span><span class="o">.</span><span class="n">group</span><span class="p">(</span><span class="s">&#39;name&#39;</span><span class="p">)</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">test</span><span class="o">.</span><span class="n">name</span><span class="p">:</span></span><a href="#l1370"></a>
<span id="l1371">            <span class="n">example</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">test</span><span class="o">.</span><span class="n">examples</span><span class="p">[</span><span class="nb">int</span><span class="p">(</span><span class="n">m</span><span class="o">.</span><span class="n">group</span><span class="p">(</span><span class="s">&#39;examplenum&#39;</span><span class="p">))]</span></span><a href="#l1371"></a>
<span id="l1372">            <span class="n">source</span> <span class="o">=</span> <span class="n">example</span><span class="o">.</span><span class="n">source</span></span><a href="#l1372"></a>
<span id="l1373">            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">source</span><span class="p">,</span> <span class="nb">unicode</span><span class="p">):</span></span><a href="#l1373"></a>
<span id="l1374">                <span class="n">source</span> <span class="o">=</span> <span class="n">source</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s">&#39;ascii&#39;</span><span class="p">,</span> <span class="s">&#39;backslashreplace&#39;</span><span class="p">)</span></span><a href="#l1374"></a>
<span id="l1375">            <span class="k">return</span> <span class="n">source</span><span class="o">.</span><span class="n">splitlines</span><span class="p">(</span><span class="bp">True</span><span class="p">)</span></span><a href="#l1375"></a>
<span id="l1376">        <span class="k">else</span><span class="p">:</span></span><a href="#l1376"></a>
<span id="l1377">            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">save_linecache_getlines</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="n">module_globals</span><span class="p">)</span></span><a href="#l1377"></a>
<span id="l1378"></span><a href="#l1378"></a>
<span id="l1379">    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">test</span><span class="p">,</span> <span class="n">compileflags</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">out</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">clear_globs</span><span class="o">=</span><span class="bp">True</span><span class="p">):</span></span><a href="#l1379"></a>
<span id="l1380">        <span class="sd">&quot;&quot;&quot;</span></span><a href="#l1380"></a>
<span id="l1381"><span class="sd">        Run the examples in `test`, and display the results using the</span></span><a href="#l1381"></a>
<span id="l1382"><span class="sd">        writer function `out`.</span></span><a href="#l1382"></a>
<span id="l1383"></span><a href="#l1383"></a>
<span id="l1384"><span class="sd">        The examples are run in the namespace `test.globs`.  If</span></span><a href="#l1384"></a>
<span id="l1385"><span class="sd">        `clear_globs` is true (the default), then this namespace will</span></span><a href="#l1385"></a>
<span id="l1386"><span class="sd">        be cleared after the test runs, to help with garbage</span></span><a href="#l1386"></a>
<span id="l1387"><span class="sd">        collection.  If you would like to examine the namespace after</span></span><a href="#l1387"></a>
<span id="l1388"><span class="sd">        the test completes, then use `clear_globs=False`.</span></span><a href="#l1388"></a>
<span id="l1389"></span><a href="#l1389"></a>
<span id="l1390"><span class="sd">        `compileflags` gives the set of flags that should be used by</span></span><a href="#l1390"></a>
<span id="l1391"><span class="sd">        the Python compiler when running the examples.  If not</span></span><a href="#l1391"></a>
<span id="l1392"><span class="sd">        specified, then it will default to the set of future-import</span></span><a href="#l1392"></a>
<span id="l1393"><span class="sd">        flags that apply to `globs`.</span></span><a href="#l1393"></a>
<span id="l1394"></span><a href="#l1394"></a>
<span id="l1395"><span class="sd">        The output of each example is checked using</span></span><a href="#l1395"></a>
<span id="l1396"><span class="sd">        `DocTestRunner.check_output`, and the results are formatted by</span></span><a href="#l1396"></a>
<span id="l1397"><span class="sd">        the `DocTestRunner.report_*` methods.</span></span><a href="#l1397"></a>
<span id="l1398"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l1398"></a>
<span id="l1399">        <span class="bp">self</span><span class="o">.</span><span class="n">test</span> <span class="o">=</span> <span class="n">test</span></span><a href="#l1399"></a>
<span id="l1400"></span><a href="#l1400"></a>
<span id="l1401">        <span class="k">if</span> <span class="n">compileflags</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1401"></a>
<span id="l1402">            <span class="n">compileflags</span> <span class="o">=</span> <span class="n">_extract_future_flags</span><span class="p">(</span><span class="n">test</span><span class="o">.</span><span class="n">globs</span><span class="p">)</span></span><a href="#l1402"></a>
<span id="l1403"></span><a href="#l1403"></a>
<span id="l1404">        <span class="n">save_stdout</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">stdout</span></span><a href="#l1404"></a>
<span id="l1405">        <span class="k">if</span> <span class="n">out</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1405"></a>
<span id="l1406">            <span class="n">out</span> <span class="o">=</span> <span class="n">save_stdout</span><span class="o">.</span><span class="n">write</span></span><a href="#l1406"></a>
<span id="l1407">        <span class="n">sys</span><span class="o">.</span><span class="n">stdout</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_fakeout</span></span><a href="#l1407"></a>
<span id="l1408"></span><a href="#l1408"></a>
<span id="l1409">        <span class="c"># Patch pdb.set_trace to restore sys.stdout during interactive</span></span><a href="#l1409"></a>
<span id="l1410">        <span class="c"># debugging (so it&#39;s not still redirected to self._fakeout).</span></span><a href="#l1410"></a>
<span id="l1411">        <span class="c"># Note that the interactive output will go to *our*</span></span><a href="#l1411"></a>
<span id="l1412">        <span class="c"># save_stdout, even if that&#39;s not the real sys.stdout; this</span></span><a href="#l1412"></a>
<span id="l1413">        <span class="c"># allows us to write test cases for the set_trace behavior.</span></span><a href="#l1413"></a>
<span id="l1414">        <span class="n">save_set_trace</span> <span class="o">=</span> <span class="n">pdb</span><span class="o">.</span><span class="n">set_trace</span></span><a href="#l1414"></a>
<span id="l1415">        <span class="bp">self</span><span class="o">.</span><span class="n">debugger</span> <span class="o">=</span> <span class="n">_OutputRedirectingPdb</span><span class="p">(</span><span class="n">save_stdout</span><span class="p">)</span></span><a href="#l1415"></a>
<span id="l1416">        <span class="bp">self</span><span class="o">.</span><span class="n">debugger</span><span class="o">.</span><span class="n">reset</span><span class="p">()</span></span><a href="#l1416"></a>
<span id="l1417">        <span class="n">pdb</span><span class="o">.</span><span class="n">set_trace</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">debugger</span><span class="o">.</span><span class="n">set_trace</span></span><a href="#l1417"></a>
<span id="l1418"></span><a href="#l1418"></a>
<span id="l1419">        <span class="c"># Patch linecache.getlines, so we can see the example&#39;s source</span></span><a href="#l1419"></a>
<span id="l1420">        <span class="c"># when we&#39;re inside the debugger.</span></span><a href="#l1420"></a>
<span id="l1421">        <span class="bp">self</span><span class="o">.</span><span class="n">save_linecache_getlines</span> <span class="o">=</span> <span class="n">linecache</span><span class="o">.</span><span class="n">getlines</span></span><a href="#l1421"></a>
<span id="l1422">        <span class="n">linecache</span><span class="o">.</span><span class="n">getlines</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__patched_linecache_getlines</span></span><a href="#l1422"></a>
<span id="l1423"></span><a href="#l1423"></a>
<span id="l1424">        <span class="c"># Make sure sys.displayhook just prints the value to stdout</span></span><a href="#l1424"></a>
<span id="l1425">        <span class="n">save_displayhook</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">displayhook</span></span><a href="#l1425"></a>
<span id="l1426">        <span class="n">sys</span><span class="o">.</span><span class="n">displayhook</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">__displayhook__</span></span><a href="#l1426"></a>
<span id="l1427"></span><a href="#l1427"></a>
<span id="l1428">        <span class="k">try</span><span class="p">:</span></span><a href="#l1428"></a>
<span id="l1429">            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">__run</span><span class="p">(</span><span class="n">test</span><span class="p">,</span> <span class="n">compileflags</span><span class="p">,</span> <span class="n">out</span><span class="p">)</span></span><a href="#l1429"></a>
<span id="l1430">        <span class="k">finally</span><span class="p">:</span></span><a href="#l1430"></a>
<span id="l1431">            <span class="n">sys</span><span class="o">.</span><span class="n">stdout</span> <span class="o">=</span> <span class="n">save_stdout</span></span><a href="#l1431"></a>
<span id="l1432">            <span class="n">pdb</span><span class="o">.</span><span class="n">set_trace</span> <span class="o">=</span> <span class="n">save_set_trace</span></span><a href="#l1432"></a>
<span id="l1433">            <span class="n">linecache</span><span class="o">.</span><span class="n">getlines</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">save_linecache_getlines</span></span><a href="#l1433"></a>
<span id="l1434">            <span class="n">sys</span><span class="o">.</span><span class="n">displayhook</span> <span class="o">=</span> <span class="n">save_displayhook</span></span><a href="#l1434"></a>
<span id="l1435">            <span class="k">if</span> <span class="n">clear_globs</span><span class="p">:</span></span><a href="#l1435"></a>
<span id="l1436">                <span class="n">test</span><span class="o">.</span><span class="n">globs</span><span class="o">.</span><span class="n">clear</span><span class="p">()</span></span><a href="#l1436"></a>
<span id="l1437"></span><a href="#l1437"></a>
<span id="l1438">    <span class="c">#/////////////////////////////////////////////////////////////////</span></span><a href="#l1438"></a>
<span id="l1439">    <span class="c"># Summarization</span></span><a href="#l1439"></a>
<span id="l1440">    <span class="c">#/////////////////////////////////////////////////////////////////</span></span><a href="#l1440"></a>
<span id="l1441">    <span class="k">def</span> <span class="nf">summarize</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">verbose</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l1441"></a>
<span id="l1442">        <span class="sd">&quot;&quot;&quot;</span></span><a href="#l1442"></a>
<span id="l1443"><span class="sd">        Print a summary of all the test cases that have been run by</span></span><a href="#l1443"></a>
<span id="l1444"><span class="sd">        this DocTestRunner, and return a tuple `(f, t)`, where `f` is</span></span><a href="#l1444"></a>
<span id="l1445"><span class="sd">        the total number of failed examples, and `t` is the total</span></span><a href="#l1445"></a>
<span id="l1446"><span class="sd">        number of tried examples.</span></span><a href="#l1446"></a>
<span id="l1447"></span><a href="#l1447"></a>
<span id="l1448"><span class="sd">        The optional `verbose` argument controls how detailed the</span></span><a href="#l1448"></a>
<span id="l1449"><span class="sd">        summary is.  If the verbosity is not specified, then the</span></span><a href="#l1449"></a>
<span id="l1450"><span class="sd">        DocTestRunner&#39;s verbosity is used.</span></span><a href="#l1450"></a>
<span id="l1451"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l1451"></a>
<span id="l1452">        <span class="k">if</span> <span class="n">verbose</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1452"></a>
<span id="l1453">            <span class="n">verbose</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span></span><a href="#l1453"></a>
<span id="l1454">        <span class="n">notests</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l1454"></a>
<span id="l1455">        <span class="n">passed</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l1455"></a>
<span id="l1456">        <span class="n">failed</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l1456"></a>
<span id="l1457">        <span class="n">totalt</span> <span class="o">=</span> <span class="n">totalf</span> <span class="o">=</span> <span class="mi">0</span></span><a href="#l1457"></a>
<span id="l1458">        <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_name2ft</span><span class="o">.</span><span class="n">items</span><span class="p">():</span></span><a href="#l1458"></a>
<span id="l1459">            <span class="n">name</span><span class="p">,</span> <span class="p">(</span><span class="n">f</span><span class="p">,</span> <span class="n">t</span><span class="p">)</span> <span class="o">=</span> <span class="n">x</span></span><a href="#l1459"></a>
<span id="l1460">            <span class="k">assert</span> <span class="n">f</span> <span class="o">&lt;=</span> <span class="n">t</span></span><a href="#l1460"></a>
<span id="l1461">            <span class="n">totalt</span> <span class="o">+=</span> <span class="n">t</span></span><a href="#l1461"></a>
<span id="l1462">            <span class="n">totalf</span> <span class="o">+=</span> <span class="n">f</span></span><a href="#l1462"></a>
<span id="l1463">            <span class="k">if</span> <span class="n">t</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span></span><a href="#l1463"></a>
<span id="l1464">                <span class="n">notests</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">name</span><span class="p">)</span></span><a href="#l1464"></a>
<span id="l1465">            <span class="k">elif</span> <span class="n">f</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span></span><a href="#l1465"></a>
<span id="l1466">                <span class="n">passed</span><span class="o">.</span><span class="n">append</span><span class="p">(</span> <span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">t</span><span class="p">)</span> <span class="p">)</span></span><a href="#l1466"></a>
<span id="l1467">            <span class="k">else</span><span class="p">:</span></span><a href="#l1467"></a>
<span id="l1468">                <span class="n">failed</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">x</span><span class="p">)</span></span><a href="#l1468"></a>
<span id="l1469">        <span class="k">if</span> <span class="n">verbose</span><span class="p">:</span></span><a href="#l1469"></a>
<span id="l1470">            <span class="k">if</span> <span class="n">notests</span><span class="p">:</span></span><a href="#l1470"></a>
<span id="l1471">                <span class="k">print</span> <span class="nb">len</span><span class="p">(</span><span class="n">notests</span><span class="p">),</span> <span class="s">&quot;items had no tests:&quot;</span></span><a href="#l1471"></a>
<span id="l1472">                <span class="n">notests</span><span class="o">.</span><span class="n">sort</span><span class="p">()</span></span><a href="#l1472"></a>
<span id="l1473">                <span class="k">for</span> <span class="n">thing</span> <span class="ow">in</span> <span class="n">notests</span><span class="p">:</span></span><a href="#l1473"></a>
<span id="l1474">                    <span class="k">print</span> <span class="s">&quot;   &quot;</span><span class="p">,</span> <span class="n">thing</span></span><a href="#l1474"></a>
<span id="l1475">            <span class="k">if</span> <span class="n">passed</span><span class="p">:</span></span><a href="#l1475"></a>
<span id="l1476">                <span class="k">print</span> <span class="nb">len</span><span class="p">(</span><span class="n">passed</span><span class="p">),</span> <span class="s">&quot;items passed all tests:&quot;</span></span><a href="#l1476"></a>
<span id="l1477">                <span class="n">passed</span><span class="o">.</span><span class="n">sort</span><span class="p">()</span></span><a href="#l1477"></a>
<span id="l1478">                <span class="k">for</span> <span class="n">thing</span><span class="p">,</span> <span class="n">count</span> <span class="ow">in</span> <span class="n">passed</span><span class="p">:</span></span><a href="#l1478"></a>
<span id="l1479">                    <span class="k">print</span> <span class="s">&quot; </span><span class="si">%3d</span><span class="s"> tests in </span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">count</span><span class="p">,</span> <span class="n">thing</span><span class="p">)</span></span><a href="#l1479"></a>
<span id="l1480">        <span class="k">if</span> <span class="n">failed</span><span class="p">:</span></span><a href="#l1480"></a>
<span id="l1481">            <span class="k">print</span> <span class="bp">self</span><span class="o">.</span><span class="n">DIVIDER</span></span><a href="#l1481"></a>
<span id="l1482">            <span class="k">print</span> <span class="nb">len</span><span class="p">(</span><span class="n">failed</span><span class="p">),</span> <span class="s">&quot;items had failures:&quot;</span></span><a href="#l1482"></a>
<span id="l1483">            <span class="n">failed</span><span class="o">.</span><span class="n">sort</span><span class="p">()</span></span><a href="#l1483"></a>
<span id="l1484">            <span class="k">for</span> <span class="n">thing</span><span class="p">,</span> <span class="p">(</span><span class="n">f</span><span class="p">,</span> <span class="n">t</span><span class="p">)</span> <span class="ow">in</span> <span class="n">failed</span><span class="p">:</span></span><a href="#l1484"></a>
<span id="l1485">                <span class="k">print</span> <span class="s">&quot; </span><span class="si">%3d</span><span class="s"> of </span><span class="si">%3d</span><span class="s"> in </span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">f</span><span class="p">,</span> <span class="n">t</span><span class="p">,</span> <span class="n">thing</span><span class="p">)</span></span><a href="#l1485"></a>
<span id="l1486">        <span class="k">if</span> <span class="n">verbose</span><span class="p">:</span></span><a href="#l1486"></a>
<span id="l1487">            <span class="k">print</span> <span class="n">totalt</span><span class="p">,</span> <span class="s">&quot;tests in&quot;</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_name2ft</span><span class="p">),</span> <span class="s">&quot;items.&quot;</span></span><a href="#l1487"></a>
<span id="l1488">            <span class="k">print</span> <span class="n">totalt</span> <span class="o">-</span> <span class="n">totalf</span><span class="p">,</span> <span class="s">&quot;passed and&quot;</span><span class="p">,</span> <span class="n">totalf</span><span class="p">,</span> <span class="s">&quot;failed.&quot;</span></span><a href="#l1488"></a>
<span id="l1489">        <span class="k">if</span> <span class="n">totalf</span><span class="p">:</span></span><a href="#l1489"></a>
<span id="l1490">            <span class="k">print</span> <span class="s">&quot;***Test Failed***&quot;</span><span class="p">,</span> <span class="n">totalf</span><span class="p">,</span> <span class="s">&quot;failures.&quot;</span></span><a href="#l1490"></a>
<span id="l1491">        <span class="k">elif</span> <span class="n">verbose</span><span class="p">:</span></span><a href="#l1491"></a>
<span id="l1492">            <span class="k">print</span> <span class="s">&quot;Test passed.&quot;</span></span><a href="#l1492"></a>
<span id="l1493">        <span class="k">return</span> <span class="n">TestResults</span><span class="p">(</span><span class="n">totalf</span><span class="p">,</span> <span class="n">totalt</span><span class="p">)</span></span><a href="#l1493"></a>
<span id="l1494"></span><a href="#l1494"></a>
<span id="l1495">    <span class="c">#/////////////////////////////////////////////////////////////////</span></span><a href="#l1495"></a>
<span id="l1496">    <span class="c"># Backward compatibility cruft to maintain doctest.master.</span></span><a href="#l1496"></a>
<span id="l1497">    <span class="c">#/////////////////////////////////////////////////////////////////</span></span><a href="#l1497"></a>
<span id="l1498">    <span class="k">def</span> <span class="nf">merge</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l1498"></a>
<span id="l1499">        <span class="n">d</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_name2ft</span></span><a href="#l1499"></a>
<span id="l1500">        <span class="k">for</span> <span class="n">name</span><span class="p">,</span> <span class="p">(</span><span class="n">f</span><span class="p">,</span> <span class="n">t</span><span class="p">)</span> <span class="ow">in</span> <span class="n">other</span><span class="o">.</span><span class="n">_name2ft</span><span class="o">.</span><span class="n">items</span><span class="p">():</span></span><a href="#l1500"></a>
<span id="l1501">            <span class="k">if</span> <span class="n">name</span> <span class="ow">in</span> <span class="n">d</span><span class="p">:</span></span><a href="#l1501"></a>
<span id="l1502">                <span class="c"># Don&#39;t print here by default, since doing</span></span><a href="#l1502"></a>
<span id="l1503">                <span class="c">#     so breaks some of the buildbots</span></span><a href="#l1503"></a>
<span id="l1504">                <span class="c">#print &quot;*** DocTestRunner.merge: &#39;&quot; + name + &quot;&#39; in both&quot; \</span></span><a href="#l1504"></a>
<span id="l1505">                <span class="c">#    &quot; testers; summing outcomes.&quot;</span></span><a href="#l1505"></a>
<span id="l1506">                <span class="n">f2</span><span class="p">,</span> <span class="n">t2</span> <span class="o">=</span> <span class="n">d</span><span class="p">[</span><span class="n">name</span><span class="p">]</span></span><a href="#l1506"></a>
<span id="l1507">                <span class="n">f</span> <span class="o">=</span> <span class="n">f</span> <span class="o">+</span> <span class="n">f2</span></span><a href="#l1507"></a>
<span id="l1508">                <span class="n">t</span> <span class="o">=</span> <span class="n">t</span> <span class="o">+</span> <span class="n">t2</span></span><a href="#l1508"></a>
<span id="l1509">            <span class="n">d</span><span class="p">[</span><span class="n">name</span><span class="p">]</span> <span class="o">=</span> <span class="n">f</span><span class="p">,</span> <span class="n">t</span></span><a href="#l1509"></a>
<span id="l1510"></span><a href="#l1510"></a>
<span id="l1511"><span class="k">class</span> <span class="nc">OutputChecker</span><span class="p">:</span></span><a href="#l1511"></a>
<span id="l1512">    <span class="sd">&quot;&quot;&quot;</span></span><a href="#l1512"></a>
<span id="l1513"><span class="sd">    A class used to check the whether the actual output from a doctest</span></span><a href="#l1513"></a>
<span id="l1514"><span class="sd">    example matches the expected output.  `OutputChecker` defines two</span></span><a href="#l1514"></a>
<span id="l1515"><span class="sd">    methods: `check_output`, which compares a given pair of outputs,</span></span><a href="#l1515"></a>
<span id="l1516"><span class="sd">    and returns true if they match; and `output_difference`, which</span></span><a href="#l1516"></a>
<span id="l1517"><span class="sd">    returns a string describing the differences between two outputs.</span></span><a href="#l1517"></a>
<span id="l1518"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l1518"></a>
<span id="l1519">    <span class="k">def</span> <span class="nf">check_output</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">want</span><span class="p">,</span> <span class="n">got</span><span class="p">,</span> <span class="n">optionflags</span><span class="p">):</span></span><a href="#l1519"></a>
<span id="l1520">        <span class="sd">&quot;&quot;&quot;</span></span><a href="#l1520"></a>
<span id="l1521"><span class="sd">        Return True iff the actual output from an example (`got`)</span></span><a href="#l1521"></a>
<span id="l1522"><span class="sd">        matches the expected output (`want`).  These strings are</span></span><a href="#l1522"></a>
<span id="l1523"><span class="sd">        always considered to match if they are identical; but</span></span><a href="#l1523"></a>
<span id="l1524"><span class="sd">        depending on what option flags the test runner is using,</span></span><a href="#l1524"></a>
<span id="l1525"><span class="sd">        several non-exact match types are also possible.  See the</span></span><a href="#l1525"></a>
<span id="l1526"><span class="sd">        documentation for `TestRunner` for more information about</span></span><a href="#l1526"></a>
<span id="l1527"><span class="sd">        option flags.</span></span><a href="#l1527"></a>
<span id="l1528"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l1528"></a>
<span id="l1529">        <span class="c"># Handle the common case first, for efficiency:</span></span><a href="#l1529"></a>
<span id="l1530">        <span class="c"># if they&#39;re string-identical, always return true.</span></span><a href="#l1530"></a>
<span id="l1531">        <span class="k">if</span> <span class="n">got</span> <span class="o">==</span> <span class="n">want</span><span class="p">:</span></span><a href="#l1531"></a>
<span id="l1532">            <span class="k">return</span> <span class="bp">True</span></span><a href="#l1532"></a>
<span id="l1533"></span><a href="#l1533"></a>
<span id="l1534">        <span class="c"># The values True and False replaced 1 and 0 as the return</span></span><a href="#l1534"></a>
<span id="l1535">        <span class="c"># value for boolean comparisons in Python 2.3.</span></span><a href="#l1535"></a>
<span id="l1536">        <span class="k">if</span> <span class="ow">not</span> <span class="p">(</span><span class="n">optionflags</span> <span class="o">&amp;</span> <span class="n">DONT_ACCEPT_TRUE_FOR_1</span><span class="p">):</span></span><a href="#l1536"></a>
<span id="l1537">            <span class="k">if</span> <span class="p">(</span><span class="n">got</span><span class="p">,</span><span class="n">want</span><span class="p">)</span> <span class="o">==</span> <span class="p">(</span><span class="s">&quot;True</span><span class="se">\n</span><span class="s">&quot;</span><span class="p">,</span> <span class="s">&quot;1</span><span class="se">\n</span><span class="s">&quot;</span><span class="p">):</span></span><a href="#l1537"></a>
<span id="l1538">                <span class="k">return</span> <span class="bp">True</span></span><a href="#l1538"></a>
<span id="l1539">            <span class="k">if</span> <span class="p">(</span><span class="n">got</span><span class="p">,</span><span class="n">want</span><span class="p">)</span> <span class="o">==</span> <span class="p">(</span><span class="s">&quot;False</span><span class="se">\n</span><span class="s">&quot;</span><span class="p">,</span> <span class="s">&quot;0</span><span class="se">\n</span><span class="s">&quot;</span><span class="p">):</span></span><a href="#l1539"></a>
<span id="l1540">                <span class="k">return</span> <span class="bp">True</span></span><a href="#l1540"></a>
<span id="l1541"></span><a href="#l1541"></a>
<span id="l1542">        <span class="c"># &lt;BLANKLINE&gt; can be used as a special sequence to signify a</span></span><a href="#l1542"></a>
<span id="l1543">        <span class="c"># blank line, unless the DONT_ACCEPT_BLANKLINE flag is used.</span></span><a href="#l1543"></a>
<span id="l1544">        <span class="k">if</span> <span class="ow">not</span> <span class="p">(</span><span class="n">optionflags</span> <span class="o">&amp;</span> <span class="n">DONT_ACCEPT_BLANKLINE</span><span class="p">):</span></span><a href="#l1544"></a>
<span id="l1545">            <span class="c"># Replace &lt;BLANKLINE&gt; in want with a blank line.</span></span><a href="#l1545"></a>
<span id="l1546">            <span class="n">want</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="s">&#39;(?m)^</span><span class="si">%s</span><span class="s">\s*?$&#39;</span> <span class="o">%</span> <span class="n">re</span><span class="o">.</span><span class="n">escape</span><span class="p">(</span><span class="n">BLANKLINE_MARKER</span><span class="p">),</span></span><a href="#l1546"></a>
<span id="l1547">                          <span class="s">&#39;&#39;</span><span class="p">,</span> <span class="n">want</span><span class="p">)</span></span><a href="#l1547"></a>
<span id="l1548">            <span class="c"># If a line in got contains only spaces, then remove the</span></span><a href="#l1548"></a>
<span id="l1549">            <span class="c"># spaces.</span></span><a href="#l1549"></a>
<span id="l1550">            <span class="n">got</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="s">&#39;(?m)^\s*?$&#39;</span><span class="p">,</span> <span class="s">&#39;&#39;</span><span class="p">,</span> <span class="n">got</span><span class="p">)</span></span><a href="#l1550"></a>
<span id="l1551">            <span class="k">if</span> <span class="n">got</span> <span class="o">==</span> <span class="n">want</span><span class="p">:</span></span><a href="#l1551"></a>
<span id="l1552">                <span class="k">return</span> <span class="bp">True</span></span><a href="#l1552"></a>
<span id="l1553"></span><a href="#l1553"></a>
<span id="l1554">        <span class="c"># This flag causes doctest to ignore any differences in the</span></span><a href="#l1554"></a>
<span id="l1555">        <span class="c"># contents of whitespace strings.  Note that this can be used</span></span><a href="#l1555"></a>
<span id="l1556">        <span class="c"># in conjunction with the ELLIPSIS flag.</span></span><a href="#l1556"></a>
<span id="l1557">        <span class="k">if</span> <span class="n">optionflags</span> <span class="o">&amp;</span> <span class="n">NORMALIZE_WHITESPACE</span><span class="p">:</span></span><a href="#l1557"></a>
<span id="l1558">            <span class="n">got</span> <span class="o">=</span> <span class="s">&#39; &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">got</span><span class="o">.</span><span class="n">split</span><span class="p">())</span></span><a href="#l1558"></a>
<span id="l1559">            <span class="n">want</span> <span class="o">=</span> <span class="s">&#39; &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">want</span><span class="o">.</span><span class="n">split</span><span class="p">())</span></span><a href="#l1559"></a>
<span id="l1560">            <span class="k">if</span> <span class="n">got</span> <span class="o">==</span> <span class="n">want</span><span class="p">:</span></span><a href="#l1560"></a>
<span id="l1561">                <span class="k">return</span> <span class="bp">True</span></span><a href="#l1561"></a>
<span id="l1562"></span><a href="#l1562"></a>
<span id="l1563">        <span class="c"># The ELLIPSIS flag says to let the sequence &quot;...&quot; in `want`</span></span><a href="#l1563"></a>
<span id="l1564">        <span class="c"># match any substring in `got`.</span></span><a href="#l1564"></a>
<span id="l1565">        <span class="k">if</span> <span class="n">optionflags</span> <span class="o">&amp;</span> <span class="n">ELLIPSIS</span><span class="p">:</span></span><a href="#l1565"></a>
<span id="l1566">            <span class="k">if</span> <span class="n">_ellipsis_match</span><span class="p">(</span><span class="n">want</span><span class="p">,</span> <span class="n">got</span><span class="p">):</span></span><a href="#l1566"></a>
<span id="l1567">                <span class="k">return</span> <span class="bp">True</span></span><a href="#l1567"></a>
<span id="l1568"></span><a href="#l1568"></a>
<span id="l1569">        <span class="c"># We didn&#39;t find any match; return false.</span></span><a href="#l1569"></a>
<span id="l1570">        <span class="k">return</span> <span class="bp">False</span></span><a href="#l1570"></a>
<span id="l1571"></span><a href="#l1571"></a>
<span id="l1572">    <span class="c"># Should we do a fancy diff?</span></span><a href="#l1572"></a>
<span id="l1573">    <span class="k">def</span> <span class="nf">_do_a_fancy_diff</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">want</span><span class="p">,</span> <span class="n">got</span><span class="p">,</span> <span class="n">optionflags</span><span class="p">):</span></span><a href="#l1573"></a>
<span id="l1574">        <span class="c"># Not unless they asked for a fancy diff.</span></span><a href="#l1574"></a>
<span id="l1575">        <span class="k">if</span> <span class="ow">not</span> <span class="n">optionflags</span> <span class="o">&amp;</span> <span class="p">(</span><span class="n">REPORT_UDIFF</span> <span class="o">|</span></span><a href="#l1575"></a>
<span id="l1576">                              <span class="n">REPORT_CDIFF</span> <span class="o">|</span></span><a href="#l1576"></a>
<span id="l1577">                              <span class="n">REPORT_NDIFF</span><span class="p">):</span></span><a href="#l1577"></a>
<span id="l1578">            <span class="k">return</span> <span class="bp">False</span></span><a href="#l1578"></a>
<span id="l1579"></span><a href="#l1579"></a>
<span id="l1580">        <span class="c"># If expected output uses ellipsis, a meaningful fancy diff is</span></span><a href="#l1580"></a>
<span id="l1581">        <span class="c"># too hard ... or maybe not.  In two real-life failures Tim saw,</span></span><a href="#l1581"></a>
<span id="l1582">        <span class="c"># a diff was a major help anyway, so this is commented out.</span></span><a href="#l1582"></a>
<span id="l1583">        <span class="c"># [todo] _ellipsis_match() knows which pieces do and don&#39;t match,</span></span><a href="#l1583"></a>
<span id="l1584">        <span class="c"># and could be the basis for a kick-ass diff in this case.</span></span><a href="#l1584"></a>
<span id="l1585">        <span class="c">##if optionflags &amp; ELLIPSIS and ELLIPSIS_MARKER in want:</span></span><a href="#l1585"></a>
<span id="l1586">        <span class="c">##    return False</span></span><a href="#l1586"></a>
<span id="l1587"></span><a href="#l1587"></a>
<span id="l1588">        <span class="c"># ndiff does intraline difference marking, so can be useful even</span></span><a href="#l1588"></a>
<span id="l1589">        <span class="c"># for 1-line differences.</span></span><a href="#l1589"></a>
<span id="l1590">        <span class="k">if</span> <span class="n">optionflags</span> <span class="o">&amp;</span> <span class="n">REPORT_NDIFF</span><span class="p">:</span></span><a href="#l1590"></a>
<span id="l1591">            <span class="k">return</span> <span class="bp">True</span></span><a href="#l1591"></a>
<span id="l1592"></span><a href="#l1592"></a>
<span id="l1593">        <span class="c"># The other diff types need at least a few lines to be helpful.</span></span><a href="#l1593"></a>
<span id="l1594">        <span class="k">return</span> <span class="n">want</span><span class="o">.</span><span class="n">count</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">2</span> <span class="ow">and</span> <span class="n">got</span><span class="o">.</span><span class="n">count</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">2</span></span><a href="#l1594"></a>
<span id="l1595"></span><a href="#l1595"></a>
<span id="l1596">    <span class="k">def</span> <span class="nf">output_difference</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">example</span><span class="p">,</span> <span class="n">got</span><span class="p">,</span> <span class="n">optionflags</span><span class="p">):</span></span><a href="#l1596"></a>
<span id="l1597">        <span class="sd">&quot;&quot;&quot;</span></span><a href="#l1597"></a>
<span id="l1598"><span class="sd">        Return a string describing the differences between the</span></span><a href="#l1598"></a>
<span id="l1599"><span class="sd">        expected output for a given example (`example`) and the actual</span></span><a href="#l1599"></a>
<span id="l1600"><span class="sd">        output (`got`).  `optionflags` is the set of option flags used</span></span><a href="#l1600"></a>
<span id="l1601"><span class="sd">        to compare `want` and `got`.</span></span><a href="#l1601"></a>
<span id="l1602"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l1602"></a>
<span id="l1603">        <span class="n">want</span> <span class="o">=</span> <span class="n">example</span><span class="o">.</span><span class="n">want</span></span><a href="#l1603"></a>
<span id="l1604">        <span class="c"># If &lt;BLANKLINE&gt;s are being used, then replace blank lines</span></span><a href="#l1604"></a>
<span id="l1605">        <span class="c"># with &lt;BLANKLINE&gt; in the actual output string.</span></span><a href="#l1605"></a>
<span id="l1606">        <span class="k">if</span> <span class="ow">not</span> <span class="p">(</span><span class="n">optionflags</span> <span class="o">&amp;</span> <span class="n">DONT_ACCEPT_BLANKLINE</span><span class="p">):</span></span><a href="#l1606"></a>
<span id="l1607">            <span class="n">got</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="s">&#39;(?m)^[ ]*(?=</span><span class="se">\n</span><span class="s">)&#39;</span><span class="p">,</span> <span class="n">BLANKLINE_MARKER</span><span class="p">,</span> <span class="n">got</span><span class="p">)</span></span><a href="#l1607"></a>
<span id="l1608"></span><a href="#l1608"></a>
<span id="l1609">        <span class="c"># Check if we should use diff.</span></span><a href="#l1609"></a>
<span id="l1610">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_do_a_fancy_diff</span><span class="p">(</span><span class="n">want</span><span class="p">,</span> <span class="n">got</span><span class="p">,</span> <span class="n">optionflags</span><span class="p">):</span></span><a href="#l1610"></a>
<span id="l1611">            <span class="c"># Split want &amp; got into lines.</span></span><a href="#l1611"></a>
<span id="l1612">            <span class="n">want_lines</span> <span class="o">=</span> <span class="n">want</span><span class="o">.</span><span class="n">splitlines</span><span class="p">(</span><span class="bp">True</span><span class="p">)</span>  <span class="c"># True == keep line ends</span></span><a href="#l1612"></a>
<span id="l1613">            <span class="n">got_lines</span> <span class="o">=</span> <span class="n">got</span><span class="o">.</span><span class="n">splitlines</span><span class="p">(</span><span class="bp">True</span><span class="p">)</span></span><a href="#l1613"></a>
<span id="l1614">            <span class="c"># Use difflib to find their differences.</span></span><a href="#l1614"></a>
<span id="l1615">            <span class="k">if</span> <span class="n">optionflags</span> <span class="o">&amp;</span> <span class="n">REPORT_UDIFF</span><span class="p">:</span></span><a href="#l1615"></a>
<span id="l1616">                <span class="n">diff</span> <span class="o">=</span> <span class="n">difflib</span><span class="o">.</span><span class="n">unified_diff</span><span class="p">(</span><span class="n">want_lines</span><span class="p">,</span> <span class="n">got_lines</span><span class="p">,</span> <span class="n">n</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span></span><a href="#l1616"></a>
<span id="l1617">                <span class="n">diff</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">diff</span><span class="p">)[</span><span class="mi">2</span><span class="p">:]</span> <span class="c"># strip the diff header</span></span><a href="#l1617"></a>
<span id="l1618">                <span class="n">kind</span> <span class="o">=</span> <span class="s">&#39;unified diff with -expected +actual&#39;</span></span><a href="#l1618"></a>
<span id="l1619">            <span class="k">elif</span> <span class="n">optionflags</span> <span class="o">&amp;</span> <span class="n">REPORT_CDIFF</span><span class="p">:</span></span><a href="#l1619"></a>
<span id="l1620">                <span class="n">diff</span> <span class="o">=</span> <span class="n">difflib</span><span class="o">.</span><span class="n">context_diff</span><span class="p">(</span><span class="n">want_lines</span><span class="p">,</span> <span class="n">got_lines</span><span class="p">,</span> <span class="n">n</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span></span><a href="#l1620"></a>
<span id="l1621">                <span class="n">diff</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">diff</span><span class="p">)[</span><span class="mi">2</span><span class="p">:]</span> <span class="c"># strip the diff header</span></span><a href="#l1621"></a>
<span id="l1622">                <span class="n">kind</span> <span class="o">=</span> <span class="s">&#39;context diff with expected followed by actual&#39;</span></span><a href="#l1622"></a>
<span id="l1623">            <span class="k">elif</span> <span class="n">optionflags</span> <span class="o">&amp;</span> <span class="n">REPORT_NDIFF</span><span class="p">:</span></span><a href="#l1623"></a>
<span id="l1624">                <span class="n">engine</span> <span class="o">=</span> <span class="n">difflib</span><span class="o">.</span><span class="n">Differ</span><span class="p">(</span><span class="n">charjunk</span><span class="o">=</span><span class="n">difflib</span><span class="o">.</span><span class="n">IS_CHARACTER_JUNK</span><span class="p">)</span></span><a href="#l1624"></a>
<span id="l1625">                <span class="n">diff</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">engine</span><span class="o">.</span><span class="n">compare</span><span class="p">(</span><span class="n">want_lines</span><span class="p">,</span> <span class="n">got_lines</span><span class="p">))</span></span><a href="#l1625"></a>
<span id="l1626">                <span class="n">kind</span> <span class="o">=</span> <span class="s">&#39;ndiff with -expected +actual&#39;</span></span><a href="#l1626"></a>
<span id="l1627">            <span class="k">else</span><span class="p">:</span></span><a href="#l1627"></a>
<span id="l1628">                <span class="k">assert</span> <span class="mi">0</span><span class="p">,</span> <span class="s">&#39;Bad diff option&#39;</span></span><a href="#l1628"></a>
<span id="l1629">            <span class="c"># Remove trailing whitespace on diff output.</span></span><a href="#l1629"></a>
<span id="l1630">            <span class="n">diff</span> <span class="o">=</span> <span class="p">[</span><span class="n">line</span><span class="o">.</span><span class="n">rstrip</span><span class="p">()</span> <span class="o">+</span> <span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span> <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">diff</span><span class="p">]</span></span><a href="#l1630"></a>
<span id="l1631">            <span class="k">return</span> <span class="s">&#39;Differences (</span><span class="si">%s</span><span class="s">):</span><span class="se">\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">kind</span> <span class="o">+</span> <span class="n">_indent</span><span class="p">(</span><span class="s">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">diff</span><span class="p">))</span></span><a href="#l1631"></a>
<span id="l1632"></span><a href="#l1632"></a>
<span id="l1633">        <span class="c"># If we&#39;re not using diff, then simply list the expected</span></span><a href="#l1633"></a>
<span id="l1634">        <span class="c"># output followed by the actual output.</span></span><a href="#l1634"></a>
<span id="l1635">        <span class="k">if</span> <span class="n">want</span> <span class="ow">and</span> <span class="n">got</span><span class="p">:</span></span><a href="#l1635"></a>
<span id="l1636">            <span class="k">return</span> <span class="s">&#39;Expected:</span><span class="se">\n</span><span class="si">%s</span><span class="s">Got:</span><span class="se">\n</span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">_indent</span><span class="p">(</span><span class="n">want</span><span class="p">),</span> <span class="n">_indent</span><span class="p">(</span><span class="n">got</span><span class="p">))</span></span><a href="#l1636"></a>
<span id="l1637">        <span class="k">elif</span> <span class="n">want</span><span class="p">:</span></span><a href="#l1637"></a>
<span id="l1638">            <span class="k">return</span> <span class="s">&#39;Expected:</span><span class="se">\n</span><span class="si">%s</span><span class="s">Got nothing</span><span class="se">\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">_indent</span><span class="p">(</span><span class="n">want</span><span class="p">)</span></span><a href="#l1638"></a>
<span id="l1639">        <span class="k">elif</span> <span class="n">got</span><span class="p">:</span></span><a href="#l1639"></a>
<span id="l1640">            <span class="k">return</span> <span class="s">&#39;Expected nothing</span><span class="se">\n</span><span class="s">Got:</span><span class="se">\n</span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">_indent</span><span class="p">(</span><span class="n">got</span><span class="p">)</span></span><a href="#l1640"></a>
<span id="l1641">        <span class="k">else</span><span class="p">:</span></span><a href="#l1641"></a>
<span id="l1642">            <span class="k">return</span> <span class="s">&#39;Expected nothing</span><span class="se">\n</span><span class="s">Got nothing</span><span class="se">\n</span><span class="s">&#39;</span></span><a href="#l1642"></a>
<span id="l1643"></span><a href="#l1643"></a>
<span id="l1644"><span class="k">class</span> <span class="nc">DocTestFailure</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span></span><a href="#l1644"></a>
<span id="l1645">    <span class="sd">&quot;&quot;&quot;A DocTest example has failed in debugging mode.</span></span><a href="#l1645"></a>
<span id="l1646"></span><a href="#l1646"></a>
<span id="l1647"><span class="sd">    The exception instance has variables:</span></span><a href="#l1647"></a>
<span id="l1648"></span><a href="#l1648"></a>
<span id="l1649"><span class="sd">    - test: the DocTest object being run</span></span><a href="#l1649"></a>
<span id="l1650"></span><a href="#l1650"></a>
<span id="l1651"><span class="sd">    - example: the Example object that failed</span></span><a href="#l1651"></a>
<span id="l1652"></span><a href="#l1652"></a>
<span id="l1653"><span class="sd">    - got: the actual output</span></span><a href="#l1653"></a>
<span id="l1654"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l1654"></a>
<span id="l1655">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">test</span><span class="p">,</span> <span class="n">example</span><span class="p">,</span> <span class="n">got</span><span class="p">):</span></span><a href="#l1655"></a>
<span id="l1656">        <span class="bp">self</span><span class="o">.</span><span class="n">test</span> <span class="o">=</span> <span class="n">test</span></span><a href="#l1656"></a>
<span id="l1657">        <span class="bp">self</span><span class="o">.</span><span class="n">example</span> <span class="o">=</span> <span class="n">example</span></span><a href="#l1657"></a>
<span id="l1658">        <span class="bp">self</span><span class="o">.</span><span class="n">got</span> <span class="o">=</span> <span class="n">got</span></span><a href="#l1658"></a>
<span id="l1659"></span><a href="#l1659"></a>
<span id="l1660">    <span class="k">def</span> <span class="nf">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1660"></a>
<span id="l1661">        <span class="k">return</span> <span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">test</span><span class="p">)</span></span><a href="#l1661"></a>
<span id="l1662"></span><a href="#l1662"></a>
<span id="l1663"><span class="k">class</span> <span class="nc">UnexpectedException</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span></span><a href="#l1663"></a>
<span id="l1664">    <span class="sd">&quot;&quot;&quot;A DocTest example has encountered an unexpected exception</span></span><a href="#l1664"></a>
<span id="l1665"></span><a href="#l1665"></a>
<span id="l1666"><span class="sd">    The exception instance has variables:</span></span><a href="#l1666"></a>
<span id="l1667"></span><a href="#l1667"></a>
<span id="l1668"><span class="sd">    - test: the DocTest object being run</span></span><a href="#l1668"></a>
<span id="l1669"></span><a href="#l1669"></a>
<span id="l1670"><span class="sd">    - example: the Example object that failed</span></span><a href="#l1670"></a>
<span id="l1671"></span><a href="#l1671"></a>
<span id="l1672"><span class="sd">    - exc_info: the exception info</span></span><a href="#l1672"></a>
<span id="l1673"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l1673"></a>
<span id="l1674">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">test</span><span class="p">,</span> <span class="n">example</span><span class="p">,</span> <span class="n">exc_info</span><span class="p">):</span></span><a href="#l1674"></a>
<span id="l1675">        <span class="bp">self</span><span class="o">.</span><span class="n">test</span> <span class="o">=</span> <span class="n">test</span></span><a href="#l1675"></a>
<span id="l1676">        <span class="bp">self</span><span class="o">.</span><span class="n">example</span> <span class="o">=</span> <span class="n">example</span></span><a href="#l1676"></a>
<span id="l1677">        <span class="bp">self</span><span class="o">.</span><span class="n">exc_info</span> <span class="o">=</span> <span class="n">exc_info</span></span><a href="#l1677"></a>
<span id="l1678"></span><a href="#l1678"></a>
<span id="l1679">    <span class="k">def</span> <span class="nf">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1679"></a>
<span id="l1680">        <span class="k">return</span> <span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">test</span><span class="p">)</span></span><a href="#l1680"></a>
<span id="l1681"></span><a href="#l1681"></a>
<span id="l1682"><span class="k">class</span> <span class="nc">DebugRunner</span><span class="p">(</span><span class="n">DocTestRunner</span><span class="p">):</span></span><a href="#l1682"></a>
<span id="l1683">    <span class="sd">r&quot;&quot;&quot;Run doc tests but raise an exception as soon as there is a failure.</span></span><a href="#l1683"></a>
<span id="l1684"></span><a href="#l1684"></a>
<span id="l1685"><span class="sd">       If an unexpected exception occurs, an UnexpectedException is raised.</span></span><a href="#l1685"></a>
<span id="l1686"><span class="sd">       It contains the test, the example, and the original exception:</span></span><a href="#l1686"></a>
<span id="l1687"></span><a href="#l1687"></a>
<span id="l1688"><span class="sd">         &gt;&gt;&gt; runner = DebugRunner(verbose=False)</span></span><a href="#l1688"></a>
<span id="l1689"><span class="sd">         &gt;&gt;&gt; test = DocTestParser().get_doctest(&#39;&gt;&gt;&gt; raise KeyError\n42&#39;,</span></span><a href="#l1689"></a>
<span id="l1690"><span class="sd">         ...                                    {}, &#39;foo&#39;, &#39;foo.py&#39;, 0)</span></span><a href="#l1690"></a>
<span id="l1691"><span class="sd">         &gt;&gt;&gt; try:</span></span><a href="#l1691"></a>
<span id="l1692"><span class="sd">         ...     runner.run(test)</span></span><a href="#l1692"></a>
<span id="l1693"><span class="sd">         ... except UnexpectedException, failure:</span></span><a href="#l1693"></a>
<span id="l1694"><span class="sd">         ...     pass</span></span><a href="#l1694"></a>
<span id="l1695"></span><a href="#l1695"></a>
<span id="l1696"><span class="sd">         &gt;&gt;&gt; failure.test is test</span></span><a href="#l1696"></a>
<span id="l1697"><span class="sd">         True</span></span><a href="#l1697"></a>
<span id="l1698"></span><a href="#l1698"></a>
<span id="l1699"><span class="sd">         &gt;&gt;&gt; failure.example.want</span></span><a href="#l1699"></a>
<span id="l1700"><span class="sd">         &#39;42\n&#39;</span></span><a href="#l1700"></a>
<span id="l1701"></span><a href="#l1701"></a>
<span id="l1702"><span class="sd">         &gt;&gt;&gt; exc_info = failure.exc_info</span></span><a href="#l1702"></a>
<span id="l1703"><span class="sd">         &gt;&gt;&gt; raise exc_info[0], exc_info[1], exc_info[2]</span></span><a href="#l1703"></a>
<span id="l1704"><span class="sd">         Traceback (most recent call last):</span></span><a href="#l1704"></a>
<span id="l1705"><span class="sd">         ...</span></span><a href="#l1705"></a>
<span id="l1706"><span class="sd">         KeyError</span></span><a href="#l1706"></a>
<span id="l1707"></span><a href="#l1707"></a>
<span id="l1708"><span class="sd">       We wrap the original exception to give the calling application</span></span><a href="#l1708"></a>
<span id="l1709"><span class="sd">       access to the test and example information.</span></span><a href="#l1709"></a>
<span id="l1710"></span><a href="#l1710"></a>
<span id="l1711"><span class="sd">       If the output doesn&#39;t match, then a DocTestFailure is raised:</span></span><a href="#l1711"></a>
<span id="l1712"></span><a href="#l1712"></a>
<span id="l1713"><span class="sd">         &gt;&gt;&gt; test = DocTestParser().get_doctest(&#39;&#39;&#39;</span></span><a href="#l1713"></a>
<span id="l1714"><span class="sd">         ...      &gt;&gt;&gt; x = 1</span></span><a href="#l1714"></a>
<span id="l1715"><span class="sd">         ...      &gt;&gt;&gt; x</span></span><a href="#l1715"></a>
<span id="l1716"><span class="sd">         ...      2</span></span><a href="#l1716"></a>
<span id="l1717"><span class="sd">         ...      &#39;&#39;&#39;, {}, &#39;foo&#39;, &#39;foo.py&#39;, 0)</span></span><a href="#l1717"></a>
<span id="l1718"></span><a href="#l1718"></a>
<span id="l1719"><span class="sd">         &gt;&gt;&gt; try:</span></span><a href="#l1719"></a>
<span id="l1720"><span class="sd">         ...    runner.run(test)</span></span><a href="#l1720"></a>
<span id="l1721"><span class="sd">         ... except DocTestFailure, failure:</span></span><a href="#l1721"></a>
<span id="l1722"><span class="sd">         ...    pass</span></span><a href="#l1722"></a>
<span id="l1723"></span><a href="#l1723"></a>
<span id="l1724"><span class="sd">       DocTestFailure objects provide access to the test:</span></span><a href="#l1724"></a>
<span id="l1725"></span><a href="#l1725"></a>
<span id="l1726"><span class="sd">         &gt;&gt;&gt; failure.test is test</span></span><a href="#l1726"></a>
<span id="l1727"><span class="sd">         True</span></span><a href="#l1727"></a>
<span id="l1728"></span><a href="#l1728"></a>
<span id="l1729"><span class="sd">       As well as to the example:</span></span><a href="#l1729"></a>
<span id="l1730"></span><a href="#l1730"></a>
<span id="l1731"><span class="sd">         &gt;&gt;&gt; failure.example.want</span></span><a href="#l1731"></a>
<span id="l1732"><span class="sd">         &#39;2\n&#39;</span></span><a href="#l1732"></a>
<span id="l1733"></span><a href="#l1733"></a>
<span id="l1734"><span class="sd">       and the actual output:</span></span><a href="#l1734"></a>
<span id="l1735"></span><a href="#l1735"></a>
<span id="l1736"><span class="sd">         &gt;&gt;&gt; failure.got</span></span><a href="#l1736"></a>
<span id="l1737"><span class="sd">         &#39;1\n&#39;</span></span><a href="#l1737"></a>
<span id="l1738"></span><a href="#l1738"></a>
<span id="l1739"><span class="sd">       If a failure or error occurs, the globals are left intact:</span></span><a href="#l1739"></a>
<span id="l1740"></span><a href="#l1740"></a>
<span id="l1741"><span class="sd">         &gt;&gt;&gt; del test.globs[&#39;__builtins__&#39;]</span></span><a href="#l1741"></a>
<span id="l1742"><span class="sd">         &gt;&gt;&gt; test.globs</span></span><a href="#l1742"></a>
<span id="l1743"><span class="sd">         {&#39;x&#39;: 1}</span></span><a href="#l1743"></a>
<span id="l1744"></span><a href="#l1744"></a>
<span id="l1745"><span class="sd">         &gt;&gt;&gt; test = DocTestParser().get_doctest(&#39;&#39;&#39;</span></span><a href="#l1745"></a>
<span id="l1746"><span class="sd">         ...      &gt;&gt;&gt; x = 2</span></span><a href="#l1746"></a>
<span id="l1747"><span class="sd">         ...      &gt;&gt;&gt; raise KeyError</span></span><a href="#l1747"></a>
<span id="l1748"><span class="sd">         ...      &#39;&#39;&#39;, {}, &#39;foo&#39;, &#39;foo.py&#39;, 0)</span></span><a href="#l1748"></a>
<span id="l1749"></span><a href="#l1749"></a>
<span id="l1750"><span class="sd">         &gt;&gt;&gt; runner.run(test)</span></span><a href="#l1750"></a>
<span id="l1751"><span class="sd">         Traceback (most recent call last):</span></span><a href="#l1751"></a>
<span id="l1752"><span class="sd">         ...</span></span><a href="#l1752"></a>
<span id="l1753"><span class="sd">         UnexpectedException: &lt;DocTest foo from foo.py:0 (2 examples)&gt;</span></span><a href="#l1753"></a>
<span id="l1754"></span><a href="#l1754"></a>
<span id="l1755"><span class="sd">         &gt;&gt;&gt; del test.globs[&#39;__builtins__&#39;]</span></span><a href="#l1755"></a>
<span id="l1756"><span class="sd">         &gt;&gt;&gt; test.globs</span></span><a href="#l1756"></a>
<span id="l1757"><span class="sd">         {&#39;x&#39;: 2}</span></span><a href="#l1757"></a>
<span id="l1758"></span><a href="#l1758"></a>
<span id="l1759"><span class="sd">       But the globals are cleared if there is no error:</span></span><a href="#l1759"></a>
<span id="l1760"></span><a href="#l1760"></a>
<span id="l1761"><span class="sd">         &gt;&gt;&gt; test = DocTestParser().get_doctest(&#39;&#39;&#39;</span></span><a href="#l1761"></a>
<span id="l1762"><span class="sd">         ...      &gt;&gt;&gt; x = 2</span></span><a href="#l1762"></a>
<span id="l1763"><span class="sd">         ...      &#39;&#39;&#39;, {}, &#39;foo&#39;, &#39;foo.py&#39;, 0)</span></span><a href="#l1763"></a>
<span id="l1764"></span><a href="#l1764"></a>
<span id="l1765"><span class="sd">         &gt;&gt;&gt; runner.run(test)</span></span><a href="#l1765"></a>
<span id="l1766"><span class="sd">         TestResults(failed=0, attempted=1)</span></span><a href="#l1766"></a>
<span id="l1767"></span><a href="#l1767"></a>
<span id="l1768"><span class="sd">         &gt;&gt;&gt; test.globs</span></span><a href="#l1768"></a>
<span id="l1769"><span class="sd">         {}</span></span><a href="#l1769"></a>
<span id="l1770"></span><a href="#l1770"></a>
<span id="l1771"><span class="sd">       &quot;&quot;&quot;</span></span><a href="#l1771"></a>
<span id="l1772"></span><a href="#l1772"></a>
<span id="l1773">    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">test</span><span class="p">,</span> <span class="n">compileflags</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">out</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">clear_globs</span><span class="o">=</span><span class="bp">True</span><span class="p">):</span></span><a href="#l1773"></a>
<span id="l1774">        <span class="n">r</span> <span class="o">=</span> <span class="n">DocTestRunner</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">test</span><span class="p">,</span> <span class="n">compileflags</span><span class="p">,</span> <span class="n">out</span><span class="p">,</span> <span class="bp">False</span><span class="p">)</span></span><a href="#l1774"></a>
<span id="l1775">        <span class="k">if</span> <span class="n">clear_globs</span><span class="p">:</span></span><a href="#l1775"></a>
<span id="l1776">            <span class="n">test</span><span class="o">.</span><span class="n">globs</span><span class="o">.</span><span class="n">clear</span><span class="p">()</span></span><a href="#l1776"></a>
<span id="l1777">        <span class="k">return</span> <span class="n">r</span></span><a href="#l1777"></a>
<span id="l1778"></span><a href="#l1778"></a>
<span id="l1779">    <span class="k">def</span> <span class="nf">report_unexpected_exception</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">out</span><span class="p">,</span> <span class="n">test</span><span class="p">,</span> <span class="n">example</span><span class="p">,</span> <span class="n">exc_info</span><span class="p">):</span></span><a href="#l1779"></a>
<span id="l1780">        <span class="k">raise</span> <span class="n">UnexpectedException</span><span class="p">(</span><span class="n">test</span><span class="p">,</span> <span class="n">example</span><span class="p">,</span> <span class="n">exc_info</span><span class="p">)</span></span><a href="#l1780"></a>
<span id="l1781"></span><a href="#l1781"></a>
<span id="l1782">    <span class="k">def</span> <span class="nf">report_failure</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">out</span><span class="p">,</span> <span class="n">test</span><span class="p">,</span> <span class="n">example</span><span class="p">,</span> <span class="n">got</span><span class="p">):</span></span><a href="#l1782"></a>
<span id="l1783">        <span class="k">raise</span> <span class="n">DocTestFailure</span><span class="p">(</span><span class="n">test</span><span class="p">,</span> <span class="n">example</span><span class="p">,</span> <span class="n">got</span><span class="p">)</span></span><a href="#l1783"></a>
<span id="l1784"></span><a href="#l1784"></a>
<span id="l1785"><span class="c">######################################################################</span></span><a href="#l1785"></a>
<span id="l1786"><span class="c">## 6. Test Functions</span></span><a href="#l1786"></a>
<span id="l1787"><span class="c">######################################################################</span></span><a href="#l1787"></a>
<span id="l1788"><span class="c"># These should be backwards compatible.</span></span><a href="#l1788"></a>
<span id="l1789"></span><a href="#l1789"></a>
<span id="l1790"><span class="c"># For backward compatibility, a global instance of a DocTestRunner</span></span><a href="#l1790"></a>
<span id="l1791"><span class="c"># class, updated by testmod.</span></span><a href="#l1791"></a>
<span id="l1792"><span class="n">master</span> <span class="o">=</span> <span class="bp">None</span></span><a href="#l1792"></a>
<span id="l1793"></span><a href="#l1793"></a>
<span id="l1794"><span class="k">def</span> <span class="nf">testmod</span><span class="p">(</span><span class="n">m</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">globs</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">verbose</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></span><a href="#l1794"></a>
<span id="l1795">            <span class="n">report</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span> <span class="n">optionflags</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">extraglobs</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></span><a href="#l1795"></a>
<span id="l1796">            <span class="n">raise_on_error</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span> <span class="n">exclude_empty</span><span class="o">=</span><span class="bp">False</span><span class="p">):</span></span><a href="#l1796"></a>
<span id="l1797">    <span class="sd">&quot;&quot;&quot;m=None, name=None, globs=None, verbose=None, report=True,</span></span><a href="#l1797"></a>
<span id="l1798"><span class="sd">       optionflags=0, extraglobs=None, raise_on_error=False,</span></span><a href="#l1798"></a>
<span id="l1799"><span class="sd">       exclude_empty=False</span></span><a href="#l1799"></a>
<span id="l1800"></span><a href="#l1800"></a>
<span id="l1801"><span class="sd">    Test examples in docstrings in functions and classes reachable</span></span><a href="#l1801"></a>
<span id="l1802"><span class="sd">    from module m (or the current module if m is not supplied), starting</span></span><a href="#l1802"></a>
<span id="l1803"><span class="sd">    with m.__doc__.</span></span><a href="#l1803"></a>
<span id="l1804"></span><a href="#l1804"></a>
<span id="l1805"><span class="sd">    Also test examples reachable from dict m.__test__ if it exists and is</span></span><a href="#l1805"></a>
<span id="l1806"><span class="sd">    not None.  m.__test__ maps names to functions, classes and strings;</span></span><a href="#l1806"></a>
<span id="l1807"><span class="sd">    function and class docstrings are tested even if the name is private;</span></span><a href="#l1807"></a>
<span id="l1808"><span class="sd">    strings are tested directly, as if they were docstrings.</span></span><a href="#l1808"></a>
<span id="l1809"></span><a href="#l1809"></a>
<span id="l1810"><span class="sd">    Return (#failures, #tests).</span></span><a href="#l1810"></a>
<span id="l1811"></span><a href="#l1811"></a>
<span id="l1812"><span class="sd">    See help(doctest) for an overview.</span></span><a href="#l1812"></a>
<span id="l1813"></span><a href="#l1813"></a>
<span id="l1814"><span class="sd">    Optional keyword arg &quot;name&quot; gives the name of the module; by default</span></span><a href="#l1814"></a>
<span id="l1815"><span class="sd">    use m.__name__.</span></span><a href="#l1815"></a>
<span id="l1816"></span><a href="#l1816"></a>
<span id="l1817"><span class="sd">    Optional keyword arg &quot;globs&quot; gives a dict to be used as the globals</span></span><a href="#l1817"></a>
<span id="l1818"><span class="sd">    when executing examples; by default, use m.__dict__.  A copy of this</span></span><a href="#l1818"></a>
<span id="l1819"><span class="sd">    dict is actually used for each docstring, so that each docstring&#39;s</span></span><a href="#l1819"></a>
<span id="l1820"><span class="sd">    examples start with a clean slate.</span></span><a href="#l1820"></a>
<span id="l1821"></span><a href="#l1821"></a>
<span id="l1822"><span class="sd">    Optional keyword arg &quot;extraglobs&quot; gives a dictionary that should be</span></span><a href="#l1822"></a>
<span id="l1823"><span class="sd">    merged into the globals that are used to execute examples.  By</span></span><a href="#l1823"></a>
<span id="l1824"><span class="sd">    default, no extra globals are used.  This is new in 2.4.</span></span><a href="#l1824"></a>
<span id="l1825"></span><a href="#l1825"></a>
<span id="l1826"><span class="sd">    Optional keyword arg &quot;verbose&quot; prints lots of stuff if true, prints</span></span><a href="#l1826"></a>
<span id="l1827"><span class="sd">    only failures if false; by default, it&#39;s true iff &quot;-v&quot; is in sys.argv.</span></span><a href="#l1827"></a>
<span id="l1828"></span><a href="#l1828"></a>
<span id="l1829"><span class="sd">    Optional keyword arg &quot;report&quot; prints a summary at the end when true,</span></span><a href="#l1829"></a>
<span id="l1830"><span class="sd">    else prints nothing at the end.  In verbose mode, the summary is</span></span><a href="#l1830"></a>
<span id="l1831"><span class="sd">    detailed, else very brief (in fact, empty if all tests passed).</span></span><a href="#l1831"></a>
<span id="l1832"></span><a href="#l1832"></a>
<span id="l1833"><span class="sd">    Optional keyword arg &quot;optionflags&quot; or&#39;s together module constants,</span></span><a href="#l1833"></a>
<span id="l1834"><span class="sd">    and defaults to 0.  This is new in 2.3.  Possible values (see the</span></span><a href="#l1834"></a>
<span id="l1835"><span class="sd">    docs for details):</span></span><a href="#l1835"></a>
<span id="l1836"></span><a href="#l1836"></a>
<span id="l1837"><span class="sd">        DONT_ACCEPT_TRUE_FOR_1</span></span><a href="#l1837"></a>
<span id="l1838"><span class="sd">        DONT_ACCEPT_BLANKLINE</span></span><a href="#l1838"></a>
<span id="l1839"><span class="sd">        NORMALIZE_WHITESPACE</span></span><a href="#l1839"></a>
<span id="l1840"><span class="sd">        ELLIPSIS</span></span><a href="#l1840"></a>
<span id="l1841"><span class="sd">        SKIP</span></span><a href="#l1841"></a>
<span id="l1842"><span class="sd">        IGNORE_EXCEPTION_DETAIL</span></span><a href="#l1842"></a>
<span id="l1843"><span class="sd">        REPORT_UDIFF</span></span><a href="#l1843"></a>
<span id="l1844"><span class="sd">        REPORT_CDIFF</span></span><a href="#l1844"></a>
<span id="l1845"><span class="sd">        REPORT_NDIFF</span></span><a href="#l1845"></a>
<span id="l1846"><span class="sd">        REPORT_ONLY_FIRST_FAILURE</span></span><a href="#l1846"></a>
<span id="l1847"></span><a href="#l1847"></a>
<span id="l1848"><span class="sd">    Optional keyword arg &quot;raise_on_error&quot; raises an exception on the</span></span><a href="#l1848"></a>
<span id="l1849"><span class="sd">    first unexpected exception or failure. This allows failures to be</span></span><a href="#l1849"></a>
<span id="l1850"><span class="sd">    post-mortem debugged.</span></span><a href="#l1850"></a>
<span id="l1851"></span><a href="#l1851"></a>
<span id="l1852"><span class="sd">    Advanced tomfoolery:  testmod runs methods of a local instance of</span></span><a href="#l1852"></a>
<span id="l1853"><span class="sd">    class doctest.Tester, then merges the results into (or creates)</span></span><a href="#l1853"></a>
<span id="l1854"><span class="sd">    global Tester instance doctest.master.  Methods of doctest.master</span></span><a href="#l1854"></a>
<span id="l1855"><span class="sd">    can be called directly too, if you want to do something unusual.</span></span><a href="#l1855"></a>
<span id="l1856"><span class="sd">    Passing report=0 to testmod is especially useful then, to delay</span></span><a href="#l1856"></a>
<span id="l1857"><span class="sd">    displaying a summary.  Invoke doctest.master.summarize(verbose)</span></span><a href="#l1857"></a>
<span id="l1858"><span class="sd">    when you&#39;re done fiddling.</span></span><a href="#l1858"></a>
<span id="l1859"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l1859"></a>
<span id="l1860">    <span class="k">global</span> <span class="n">master</span></span><a href="#l1860"></a>
<span id="l1861"></span><a href="#l1861"></a>
<span id="l1862">    <span class="c"># If no module was given, then use __main__.</span></span><a href="#l1862"></a>
<span id="l1863">    <span class="k">if</span> <span class="n">m</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1863"></a>
<span id="l1864">        <span class="c"># DWA - m will still be None if this wasn&#39;t invoked from the command</span></span><a href="#l1864"></a>
<span id="l1865">        <span class="c"># line, in which case the following TypeError is about as good an error</span></span><a href="#l1865"></a>
<span id="l1866">        <span class="c"># as we should expect</span></span><a href="#l1866"></a>
<span id="l1867">        <span class="n">m</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">modules</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;__main__&#39;</span><span class="p">)</span></span><a href="#l1867"></a>
<span id="l1868"></span><a href="#l1868"></a>
<span id="l1869">    <span class="c"># Check that we were actually given a module.</span></span><a href="#l1869"></a>
<span id="l1870">    <span class="k">if</span> <span class="ow">not</span> <span class="n">inspect</span><span class="o">.</span><span class="n">ismodule</span><span class="p">(</span><span class="n">m</span><span class="p">):</span></span><a href="#l1870"></a>
<span id="l1871">        <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="s">&quot;testmod: module required; </span><span class="si">%r</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">m</span><span class="p">,))</span></span><a href="#l1871"></a>
<span id="l1872"></span><a href="#l1872"></a>
<span id="l1873">    <span class="c"># If no name was given, then use the module&#39;s name.</span></span><a href="#l1873"></a>
<span id="l1874">    <span class="k">if</span> <span class="n">name</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1874"></a>
<span id="l1875">        <span class="n">name</span> <span class="o">=</span> <span class="n">m</span><span class="o">.</span><span class="n">__name__</span></span><a href="#l1875"></a>
<span id="l1876"></span><a href="#l1876"></a>
<span id="l1877">    <span class="c"># Find, parse, and run all tests in the given module.</span></span><a href="#l1877"></a>
<span id="l1878">    <span class="n">finder</span> <span class="o">=</span> <span class="n">DocTestFinder</span><span class="p">(</span><span class="n">exclude_empty</span><span class="o">=</span><span class="n">exclude_empty</span><span class="p">)</span></span><a href="#l1878"></a>
<span id="l1879"></span><a href="#l1879"></a>
<span id="l1880">    <span class="k">if</span> <span class="n">raise_on_error</span><span class="p">:</span></span><a href="#l1880"></a>
<span id="l1881">        <span class="n">runner</span> <span class="o">=</span> <span class="n">DebugRunner</span><span class="p">(</span><span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span> <span class="n">optionflags</span><span class="o">=</span><span class="n">optionflags</span><span class="p">)</span></span><a href="#l1881"></a>
<span id="l1882">    <span class="k">else</span><span class="p">:</span></span><a href="#l1882"></a>
<span id="l1883">        <span class="n">runner</span> <span class="o">=</span> <span class="n">DocTestRunner</span><span class="p">(</span><span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span> <span class="n">optionflags</span><span class="o">=</span><span class="n">optionflags</span><span class="p">)</span></span><a href="#l1883"></a>
<span id="l1884"></span><a href="#l1884"></a>
<span id="l1885">    <span class="k">for</span> <span class="n">test</span> <span class="ow">in</span> <span class="n">finder</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="n">m</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">globs</span><span class="o">=</span><span class="n">globs</span><span class="p">,</span> <span class="n">extraglobs</span><span class="o">=</span><span class="n">extraglobs</span><span class="p">):</span></span><a href="#l1885"></a>
<span id="l1886">        <span class="n">runner</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">test</span><span class="p">)</span></span><a href="#l1886"></a>
<span id="l1887"></span><a href="#l1887"></a>
<span id="l1888">    <span class="k">if</span> <span class="n">report</span><span class="p">:</span></span><a href="#l1888"></a>
<span id="l1889">        <span class="n">runner</span><span class="o">.</span><span class="n">summarize</span><span class="p">()</span></span><a href="#l1889"></a>
<span id="l1890"></span><a href="#l1890"></a>
<span id="l1891">    <span class="k">if</span> <span class="n">master</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1891"></a>
<span id="l1892">        <span class="n">master</span> <span class="o">=</span> <span class="n">runner</span></span><a href="#l1892"></a>
<span id="l1893">    <span class="k">else</span><span class="p">:</span></span><a href="#l1893"></a>
<span id="l1894">        <span class="n">master</span><span class="o">.</span><span class="n">merge</span><span class="p">(</span><span class="n">runner</span><span class="p">)</span></span><a href="#l1894"></a>
<span id="l1895"></span><a href="#l1895"></a>
<span id="l1896">    <span class="k">return</span> <span class="n">TestResults</span><span class="p">(</span><span class="n">runner</span><span class="o">.</span><span class="n">failures</span><span class="p">,</span> <span class="n">runner</span><span class="o">.</span><span class="n">tries</span><span class="p">)</span></span><a href="#l1896"></a>
<span id="l1897"></span><a href="#l1897"></a>
<span id="l1898"><span class="k">def</span> <span class="nf">testfile</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="n">module_relative</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">package</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></span><a href="#l1898"></a>
<span id="l1899">             <span class="n">globs</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">verbose</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">report</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span> <span class="n">optionflags</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span></span><a href="#l1899"></a>
<span id="l1900">             <span class="n">extraglobs</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">raise_on_error</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span> <span class="n">parser</span><span class="o">=</span><span class="n">DocTestParser</span><span class="p">(),</span></span><a href="#l1900"></a>
<span id="l1901">             <span class="n">encoding</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l1901"></a>
<span id="l1902">    <span class="sd">&quot;&quot;&quot;</span></span><a href="#l1902"></a>
<span id="l1903"><span class="sd">    Test examples in the given file.  Return (#failures, #tests).</span></span><a href="#l1903"></a>
<span id="l1904"></span><a href="#l1904"></a>
<span id="l1905"><span class="sd">    Optional keyword arg &quot;module_relative&quot; specifies how filenames</span></span><a href="#l1905"></a>
<span id="l1906"><span class="sd">    should be interpreted:</span></span><a href="#l1906"></a>
<span id="l1907"></span><a href="#l1907"></a>
<span id="l1908"><span class="sd">      - If &quot;module_relative&quot; is True (the default), then &quot;filename&quot;</span></span><a href="#l1908"></a>
<span id="l1909"><span class="sd">         specifies a module-relative path.  By default, this path is</span></span><a href="#l1909"></a>
<span id="l1910"><span class="sd">         relative to the calling module&#39;s directory; but if the</span></span><a href="#l1910"></a>
<span id="l1911"><span class="sd">         &quot;package&quot; argument is specified, then it is relative to that</span></span><a href="#l1911"></a>
<span id="l1912"><span class="sd">         package.  To ensure os-independence, &quot;filename&quot; should use</span></span><a href="#l1912"></a>
<span id="l1913"><span class="sd">         &quot;/&quot; characters to separate path segments, and should not</span></span><a href="#l1913"></a>
<span id="l1914"><span class="sd">         be an absolute path (i.e., it may not begin with &quot;/&quot;).</span></span><a href="#l1914"></a>
<span id="l1915"></span><a href="#l1915"></a>
<span id="l1916"><span class="sd">      - If &quot;module_relative&quot; is False, then &quot;filename&quot; specifies an</span></span><a href="#l1916"></a>
<span id="l1917"><span class="sd">        os-specific path.  The path may be absolute or relative (to</span></span><a href="#l1917"></a>
<span id="l1918"><span class="sd">        the current working directory).</span></span><a href="#l1918"></a>
<span id="l1919"></span><a href="#l1919"></a>
<span id="l1920"><span class="sd">    Optional keyword arg &quot;name&quot; gives the name of the test; by default</span></span><a href="#l1920"></a>
<span id="l1921"><span class="sd">    use the file&#39;s basename.</span></span><a href="#l1921"></a>
<span id="l1922"></span><a href="#l1922"></a>
<span id="l1923"><span class="sd">    Optional keyword argument &quot;package&quot; is a Python package or the</span></span><a href="#l1923"></a>
<span id="l1924"><span class="sd">    name of a Python package whose directory should be used as the</span></span><a href="#l1924"></a>
<span id="l1925"><span class="sd">    base directory for a module relative filename.  If no package is</span></span><a href="#l1925"></a>
<span id="l1926"><span class="sd">    specified, then the calling module&#39;s directory is used as the base</span></span><a href="#l1926"></a>
<span id="l1927"><span class="sd">    directory for module relative filenames.  It is an error to</span></span><a href="#l1927"></a>
<span id="l1928"><span class="sd">    specify &quot;package&quot; if &quot;module_relative&quot; is False.</span></span><a href="#l1928"></a>
<span id="l1929"></span><a href="#l1929"></a>
<span id="l1930"><span class="sd">    Optional keyword arg &quot;globs&quot; gives a dict to be used as the globals</span></span><a href="#l1930"></a>
<span id="l1931"><span class="sd">    when executing examples; by default, use {}.  A copy of this dict</span></span><a href="#l1931"></a>
<span id="l1932"><span class="sd">    is actually used for each docstring, so that each docstring&#39;s</span></span><a href="#l1932"></a>
<span id="l1933"><span class="sd">    examples start with a clean slate.</span></span><a href="#l1933"></a>
<span id="l1934"></span><a href="#l1934"></a>
<span id="l1935"><span class="sd">    Optional keyword arg &quot;extraglobs&quot; gives a dictionary that should be</span></span><a href="#l1935"></a>
<span id="l1936"><span class="sd">    merged into the globals that are used to execute examples.  By</span></span><a href="#l1936"></a>
<span id="l1937"><span class="sd">    default, no extra globals are used.</span></span><a href="#l1937"></a>
<span id="l1938"></span><a href="#l1938"></a>
<span id="l1939"><span class="sd">    Optional keyword arg &quot;verbose&quot; prints lots of stuff if true, prints</span></span><a href="#l1939"></a>
<span id="l1940"><span class="sd">    only failures if false; by default, it&#39;s true iff &quot;-v&quot; is in sys.argv.</span></span><a href="#l1940"></a>
<span id="l1941"></span><a href="#l1941"></a>
<span id="l1942"><span class="sd">    Optional keyword arg &quot;report&quot; prints a summary at the end when true,</span></span><a href="#l1942"></a>
<span id="l1943"><span class="sd">    else prints nothing at the end.  In verbose mode, the summary is</span></span><a href="#l1943"></a>
<span id="l1944"><span class="sd">    detailed, else very brief (in fact, empty if all tests passed).</span></span><a href="#l1944"></a>
<span id="l1945"></span><a href="#l1945"></a>
<span id="l1946"><span class="sd">    Optional keyword arg &quot;optionflags&quot; or&#39;s together module constants,</span></span><a href="#l1946"></a>
<span id="l1947"><span class="sd">    and defaults to 0.  Possible values (see the docs for details):</span></span><a href="#l1947"></a>
<span id="l1948"></span><a href="#l1948"></a>
<span id="l1949"><span class="sd">        DONT_ACCEPT_TRUE_FOR_1</span></span><a href="#l1949"></a>
<span id="l1950"><span class="sd">        DONT_ACCEPT_BLANKLINE</span></span><a href="#l1950"></a>
<span id="l1951"><span class="sd">        NORMALIZE_WHITESPACE</span></span><a href="#l1951"></a>
<span id="l1952"><span class="sd">        ELLIPSIS</span></span><a href="#l1952"></a>
<span id="l1953"><span class="sd">        SKIP</span></span><a href="#l1953"></a>
<span id="l1954"><span class="sd">        IGNORE_EXCEPTION_DETAIL</span></span><a href="#l1954"></a>
<span id="l1955"><span class="sd">        REPORT_UDIFF</span></span><a href="#l1955"></a>
<span id="l1956"><span class="sd">        REPORT_CDIFF</span></span><a href="#l1956"></a>
<span id="l1957"><span class="sd">        REPORT_NDIFF</span></span><a href="#l1957"></a>
<span id="l1958"><span class="sd">        REPORT_ONLY_FIRST_FAILURE</span></span><a href="#l1958"></a>
<span id="l1959"></span><a href="#l1959"></a>
<span id="l1960"><span class="sd">    Optional keyword arg &quot;raise_on_error&quot; raises an exception on the</span></span><a href="#l1960"></a>
<span id="l1961"><span class="sd">    first unexpected exception or failure. This allows failures to be</span></span><a href="#l1961"></a>
<span id="l1962"><span class="sd">    post-mortem debugged.</span></span><a href="#l1962"></a>
<span id="l1963"></span><a href="#l1963"></a>
<span id="l1964"><span class="sd">    Optional keyword arg &quot;parser&quot; specifies a DocTestParser (or</span></span><a href="#l1964"></a>
<span id="l1965"><span class="sd">    subclass) that should be used to extract tests from the files.</span></span><a href="#l1965"></a>
<span id="l1966"></span><a href="#l1966"></a>
<span id="l1967"><span class="sd">    Optional keyword arg &quot;encoding&quot; specifies an encoding that should</span></span><a href="#l1967"></a>
<span id="l1968"><span class="sd">    be used to convert the file to unicode.</span></span><a href="#l1968"></a>
<span id="l1969"></span><a href="#l1969"></a>
<span id="l1970"><span class="sd">    Advanced tomfoolery:  testmod runs methods of a local instance of</span></span><a href="#l1970"></a>
<span id="l1971"><span class="sd">    class doctest.Tester, then merges the results into (or creates)</span></span><a href="#l1971"></a>
<span id="l1972"><span class="sd">    global Tester instance doctest.master.  Methods of doctest.master</span></span><a href="#l1972"></a>
<span id="l1973"><span class="sd">    can be called directly too, if you want to do something unusual.</span></span><a href="#l1973"></a>
<span id="l1974"><span class="sd">    Passing report=0 to testmod is especially useful then, to delay</span></span><a href="#l1974"></a>
<span id="l1975"><span class="sd">    displaying a summary.  Invoke doctest.master.summarize(verbose)</span></span><a href="#l1975"></a>
<span id="l1976"><span class="sd">    when you&#39;re done fiddling.</span></span><a href="#l1976"></a>
<span id="l1977"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l1977"></a>
<span id="l1978">    <span class="k">global</span> <span class="n">master</span></span><a href="#l1978"></a>
<span id="l1979"></span><a href="#l1979"></a>
<span id="l1980">    <span class="k">if</span> <span class="n">package</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">module_relative</span><span class="p">:</span></span><a href="#l1980"></a>
<span id="l1981">        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&quot;Package may only be specified for module-&quot;</span></span><a href="#l1981"></a>
<span id="l1982">                         <span class="s">&quot;relative paths.&quot;</span><span class="p">)</span></span><a href="#l1982"></a>
<span id="l1983"></span><a href="#l1983"></a>
<span id="l1984">    <span class="c"># Relativize the path</span></span><a href="#l1984"></a>
<span id="l1985">    <span class="n">text</span><span class="p">,</span> <span class="n">filename</span> <span class="o">=</span> <span class="n">_load_testfile</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="n">package</span><span class="p">,</span> <span class="n">module_relative</span><span class="p">)</span></span><a href="#l1985"></a>
<span id="l1986"></span><a href="#l1986"></a>
<span id="l1987">    <span class="c"># If no name was given, then use the file&#39;s name.</span></span><a href="#l1987"></a>
<span id="l1988">    <span class="k">if</span> <span class="n">name</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1988"></a>
<span id="l1989">        <span class="n">name</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">basename</span><span class="p">(</span><span class="n">filename</span><span class="p">)</span></span><a href="#l1989"></a>
<span id="l1990"></span><a href="#l1990"></a>
<span id="l1991">    <span class="c"># Assemble the globals.</span></span><a href="#l1991"></a>
<span id="l1992">    <span class="k">if</span> <span class="n">globs</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1992"></a>
<span id="l1993">        <span class="n">globs</span> <span class="o">=</span> <span class="p">{}</span></span><a href="#l1993"></a>
<span id="l1994">    <span class="k">else</span><span class="p">:</span></span><a href="#l1994"></a>
<span id="l1995">        <span class="n">globs</span> <span class="o">=</span> <span class="n">globs</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span></span><a href="#l1995"></a>
<span id="l1996">    <span class="k">if</span> <span class="n">extraglobs</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1996"></a>
<span id="l1997">        <span class="n">globs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">extraglobs</span><span class="p">)</span></span><a href="#l1997"></a>
<span id="l1998">    <span class="k">if</span> <span class="s">&#39;__name__&#39;</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">globs</span><span class="p">:</span></span><a href="#l1998"></a>
<span id="l1999">        <span class="n">globs</span><span class="p">[</span><span class="s">&#39;__name__&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="s">&#39;__main__&#39;</span></span><a href="#l1999"></a>
<span id="l2000"></span><a href="#l2000"></a>
<span id="l2001">    <span class="k">if</span> <span class="n">raise_on_error</span><span class="p">:</span></span><a href="#l2001"></a>
<span id="l2002">        <span class="n">runner</span> <span class="o">=</span> <span class="n">DebugRunner</span><span class="p">(</span><span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span> <span class="n">optionflags</span><span class="o">=</span><span class="n">optionflags</span><span class="p">)</span></span><a href="#l2002"></a>
<span id="l2003">    <span class="k">else</span><span class="p">:</span></span><a href="#l2003"></a>
<span id="l2004">        <span class="n">runner</span> <span class="o">=</span> <span class="n">DocTestRunner</span><span class="p">(</span><span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span> <span class="n">optionflags</span><span class="o">=</span><span class="n">optionflags</span><span class="p">)</span></span><a href="#l2004"></a>
<span id="l2005"></span><a href="#l2005"></a>
<span id="l2006">    <span class="k">if</span> <span class="n">encoding</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l2006"></a>
<span id="l2007">        <span class="n">text</span> <span class="o">=</span> <span class="n">text</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="n">encoding</span><span class="p">)</span></span><a href="#l2007"></a>
<span id="l2008"></span><a href="#l2008"></a>
<span id="l2009">    <span class="c"># Read the file, convert it to a test, and run it.</span></span><a href="#l2009"></a>
<span id="l2010">    <span class="n">test</span> <span class="o">=</span> <span class="n">parser</span><span class="o">.</span><span class="n">get_doctest</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="n">globs</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">filename</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span></span><a href="#l2010"></a>
<span id="l2011">    <span class="n">runner</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">test</span><span class="p">)</span></span><a href="#l2011"></a>
<span id="l2012"></span><a href="#l2012"></a>
<span id="l2013">    <span class="k">if</span> <span class="n">report</span><span class="p">:</span></span><a href="#l2013"></a>
<span id="l2014">        <span class="n">runner</span><span class="o">.</span><span class="n">summarize</span><span class="p">()</span></span><a href="#l2014"></a>
<span id="l2015"></span><a href="#l2015"></a>
<span id="l2016">    <span class="k">if</span> <span class="n">master</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l2016"></a>
<span id="l2017">        <span class="n">master</span> <span class="o">=</span> <span class="n">runner</span></span><a href="#l2017"></a>
<span id="l2018">    <span class="k">else</span><span class="p">:</span></span><a href="#l2018"></a>
<span id="l2019">        <span class="n">master</span><span class="o">.</span><span class="n">merge</span><span class="p">(</span><span class="n">runner</span><span class="p">)</span></span><a href="#l2019"></a>
<span id="l2020"></span><a href="#l2020"></a>
<span id="l2021">    <span class="k">return</span> <span class="n">TestResults</span><span class="p">(</span><span class="n">runner</span><span class="o">.</span><span class="n">failures</span><span class="p">,</span> <span class="n">runner</span><span class="o">.</span><span class="n">tries</span><span class="p">)</span></span><a href="#l2021"></a>
<span id="l2022"></span><a href="#l2022"></a>
<span id="l2023"><span class="k">def</span> <span class="nf">run_docstring_examples</span><span class="p">(</span><span class="n">f</span><span class="p">,</span> <span class="n">globs</span><span class="p">,</span> <span class="n">verbose</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s">&quot;NoName&quot;</span><span class="p">,</span></span><a href="#l2023"></a>
<span id="l2024">                           <span class="n">compileflags</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">optionflags</span><span class="o">=</span><span class="mi">0</span><span class="p">):</span></span><a href="#l2024"></a>
<span id="l2025">    <span class="sd">&quot;&quot;&quot;</span></span><a href="#l2025"></a>
<span id="l2026"><span class="sd">    Test examples in the given object&#39;s docstring (`f`), using `globs`</span></span><a href="#l2026"></a>
<span id="l2027"><span class="sd">    as globals.  Optional argument `name` is used in failure messages.</span></span><a href="#l2027"></a>
<span id="l2028"><span class="sd">    If the optional argument `verbose` is true, then generate output</span></span><a href="#l2028"></a>
<span id="l2029"><span class="sd">    even if there are no failures.</span></span><a href="#l2029"></a>
<span id="l2030"></span><a href="#l2030"></a>
<span id="l2031"><span class="sd">    `compileflags` gives the set of flags that should be used by the</span></span><a href="#l2031"></a>
<span id="l2032"><span class="sd">    Python compiler when running the examples.  If not specified, then</span></span><a href="#l2032"></a>
<span id="l2033"><span class="sd">    it will default to the set of future-import flags that apply to</span></span><a href="#l2033"></a>
<span id="l2034"><span class="sd">    `globs`.</span></span><a href="#l2034"></a>
<span id="l2035"></span><a href="#l2035"></a>
<span id="l2036"><span class="sd">    Optional keyword arg `optionflags` specifies options for the</span></span><a href="#l2036"></a>
<span id="l2037"><span class="sd">    testing and output.  See the documentation for `testmod` for more</span></span><a href="#l2037"></a>
<span id="l2038"><span class="sd">    information.</span></span><a href="#l2038"></a>
<span id="l2039"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l2039"></a>
<span id="l2040">    <span class="c"># Find, parse, and run all tests in the given module.</span></span><a href="#l2040"></a>
<span id="l2041">    <span class="n">finder</span> <span class="o">=</span> <span class="n">DocTestFinder</span><span class="p">(</span><span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span> <span class="n">recurse</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span></span><a href="#l2041"></a>
<span id="l2042">    <span class="n">runner</span> <span class="o">=</span> <span class="n">DocTestRunner</span><span class="p">(</span><span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span> <span class="n">optionflags</span><span class="o">=</span><span class="n">optionflags</span><span class="p">)</span></span><a href="#l2042"></a>
<span id="l2043">    <span class="k">for</span> <span class="n">test</span> <span class="ow">in</span> <span class="n">finder</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="n">f</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">globs</span><span class="o">=</span><span class="n">globs</span><span class="p">):</span></span><a href="#l2043"></a>
<span id="l2044">        <span class="n">runner</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">test</span><span class="p">,</span> <span class="n">compileflags</span><span class="o">=</span><span class="n">compileflags</span><span class="p">)</span></span><a href="#l2044"></a>
<span id="l2045"></span><a href="#l2045"></a>
<span id="l2046"><span class="c">######################################################################</span></span><a href="#l2046"></a>
<span id="l2047"><span class="c">## 7. Tester</span></span><a href="#l2047"></a>
<span id="l2048"><span class="c">######################################################################</span></span><a href="#l2048"></a>
<span id="l2049"><span class="c"># This is provided only for backwards compatibility.  It&#39;s not</span></span><a href="#l2049"></a>
<span id="l2050"><span class="c"># actually used in any way.</span></span><a href="#l2050"></a>
<span id="l2051"></span><a href="#l2051"></a>
<span id="l2052"><span class="k">class</span> <span class="nc">Tester</span><span class="p">:</span></span><a href="#l2052"></a>
<span id="l2053">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">mod</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">globs</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">verbose</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">optionflags</span><span class="o">=</span><span class="mi">0</span><span class="p">):</span></span><a href="#l2053"></a>
<span id="l2054"></span><a href="#l2054"></a>
<span id="l2055">        <span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span><span class="s">&quot;class Tester is deprecated; &quot;</span></span><a href="#l2055"></a>
<span id="l2056">                      <span class="s">&quot;use class doctest.DocTestRunner instead&quot;</span><span class="p">,</span></span><a href="#l2056"></a>
<span id="l2057">                      <span class="ne">DeprecationWarning</span><span class="p">,</span> <span class="n">stacklevel</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span></span><a href="#l2057"></a>
<span id="l2058">        <span class="k">if</span> <span class="n">mod</span> <span class="ow">is</span> <span class="bp">None</span> <span class="ow">and</span> <span class="n">globs</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l2058"></a>
<span id="l2059">            <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="s">&quot;Tester.__init__: must specify mod or globs&quot;</span><span class="p">)</span></span><a href="#l2059"></a>
<span id="l2060">        <span class="k">if</span> <span class="n">mod</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">inspect</span><span class="o">.</span><span class="n">ismodule</span><span class="p">(</span><span class="n">mod</span><span class="p">):</span></span><a href="#l2060"></a>
<span id="l2061">            <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="s">&quot;Tester.__init__: mod must be a module; </span><span class="si">%r</span><span class="s">&quot;</span> <span class="o">%</span></span><a href="#l2061"></a>
<span id="l2062">                            <span class="p">(</span><span class="n">mod</span><span class="p">,))</span></span><a href="#l2062"></a>
<span id="l2063">        <span class="k">if</span> <span class="n">globs</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l2063"></a>
<span id="l2064">            <span class="n">globs</span> <span class="o">=</span> <span class="n">mod</span><span class="o">.</span><span class="n">__dict__</span></span><a href="#l2064"></a>
<span id="l2065">        <span class="bp">self</span><span class="o">.</span><span class="n">globs</span> <span class="o">=</span> <span class="n">globs</span></span><a href="#l2065"></a>
<span id="l2066"></span><a href="#l2066"></a>
<span id="l2067">        <span class="bp">self</span><span class="o">.</span><span class="n">verbose</span> <span class="o">=</span> <span class="n">verbose</span></span><a href="#l2067"></a>
<span id="l2068">        <span class="bp">self</span><span class="o">.</span><span class="n">optionflags</span> <span class="o">=</span> <span class="n">optionflags</span></span><a href="#l2068"></a>
<span id="l2069">        <span class="bp">self</span><span class="o">.</span><span class="n">testfinder</span> <span class="o">=</span> <span class="n">DocTestFinder</span><span class="p">()</span></span><a href="#l2069"></a>
<span id="l2070">        <span class="bp">self</span><span class="o">.</span><span class="n">testrunner</span> <span class="o">=</span> <span class="n">DocTestRunner</span><span class="p">(</span><span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span></span><a href="#l2070"></a>
<span id="l2071">                                        <span class="n">optionflags</span><span class="o">=</span><span class="n">optionflags</span><span class="p">)</span></span><a href="#l2071"></a>
<span id="l2072"></span><a href="#l2072"></a>
<span id="l2073">    <span class="k">def</span> <span class="nf">runstring</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">s</span><span class="p">,</span> <span class="n">name</span><span class="p">):</span></span><a href="#l2073"></a>
<span id="l2074">        <span class="n">test</span> <span class="o">=</span> <span class="n">DocTestParser</span><span class="p">()</span><span class="o">.</span><span class="n">get_doctest</span><span class="p">(</span><span class="n">s</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">globs</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="bp">None</span><span class="p">,</span> <span class="bp">None</span><span class="p">)</span></span><a href="#l2074"></a>
<span id="l2075">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">verbose</span><span class="p">:</span></span><a href="#l2075"></a>
<span id="l2076">            <span class="k">print</span> <span class="s">&quot;Running string&quot;</span><span class="p">,</span> <span class="n">name</span></span><a href="#l2076"></a>
<span id="l2077">        <span class="p">(</span><span class="n">f</span><span class="p">,</span><span class="n">t</span><span class="p">)</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">testrunner</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">test</span><span class="p">)</span></span><a href="#l2077"></a>
<span id="l2078">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">verbose</span><span class="p">:</span></span><a href="#l2078"></a>
<span id="l2079">            <span class="k">print</span> <span class="n">f</span><span class="p">,</span> <span class="s">&quot;of&quot;</span><span class="p">,</span> <span class="n">t</span><span class="p">,</span> <span class="s">&quot;examples failed in string&quot;</span><span class="p">,</span> <span class="n">name</span></span><a href="#l2079"></a>
<span id="l2080">        <span class="k">return</span> <span class="n">TestResults</span><span class="p">(</span><span class="n">f</span><span class="p">,</span><span class="n">t</span><span class="p">)</span></span><a href="#l2080"></a>
<span id="l2081"></span><a href="#l2081"></a>
<span id="l2082">    <span class="k">def</span> <span class="nf">rundoc</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">object</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">module</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l2082"></a>
<span id="l2083">        <span class="n">f</span> <span class="o">=</span> <span class="n">t</span> <span class="o">=</span> <span class="mi">0</span></span><a href="#l2083"></a>
<span id="l2084">        <span class="n">tests</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">testfinder</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="nb">object</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">module</span><span class="o">=</span><span class="n">module</span><span class="p">,</span></span><a href="#l2084"></a>
<span id="l2085">                                     <span class="n">globs</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">globs</span><span class="p">)</span></span><a href="#l2085"></a>
<span id="l2086">        <span class="k">for</span> <span class="n">test</span> <span class="ow">in</span> <span class="n">tests</span><span class="p">:</span></span><a href="#l2086"></a>
<span id="l2087">            <span class="p">(</span><span class="n">f2</span><span class="p">,</span> <span class="n">t2</span><span class="p">)</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">testrunner</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">test</span><span class="p">)</span></span><a href="#l2087"></a>
<span id="l2088">            <span class="p">(</span><span class="n">f</span><span class="p">,</span><span class="n">t</span><span class="p">)</span> <span class="o">=</span> <span class="p">(</span><span class="n">f</span><span class="o">+</span><span class="n">f2</span><span class="p">,</span> <span class="n">t</span><span class="o">+</span><span class="n">t2</span><span class="p">)</span></span><a href="#l2088"></a>
<span id="l2089">        <span class="k">return</span> <span class="n">TestResults</span><span class="p">(</span><span class="n">f</span><span class="p">,</span><span class="n">t</span><span class="p">)</span></span><a href="#l2089"></a>
<span id="l2090"></span><a href="#l2090"></a>
<span id="l2091">    <span class="k">def</span> <span class="nf">rundict</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">d</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">module</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l2091"></a>
<span id="l2092">        <span class="kn">import</span> <span class="nn">types</span></span><a href="#l2092"></a>
<span id="l2093">        <span class="n">m</span> <span class="o">=</span> <span class="n">types</span><span class="o">.</span><span class="n">ModuleType</span><span class="p">(</span><span class="n">name</span><span class="p">)</span></span><a href="#l2093"></a>
<span id="l2094">        <span class="n">m</span><span class="o">.</span><span class="n">__dict__</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">d</span><span class="p">)</span></span><a href="#l2094"></a>
<span id="l2095">        <span class="k">if</span> <span class="n">module</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l2095"></a>
<span id="l2096">            <span class="n">module</span> <span class="o">=</span> <span class="bp">False</span></span><a href="#l2096"></a>
<span id="l2097">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">rundoc</span><span class="p">(</span><span class="n">m</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">module</span><span class="p">)</span></span><a href="#l2097"></a>
<span id="l2098"></span><a href="#l2098"></a>
<span id="l2099">    <span class="k">def</span> <span class="nf">run__test__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">d</span><span class="p">,</span> <span class="n">name</span><span class="p">):</span></span><a href="#l2099"></a>
<span id="l2100">        <span class="kn">import</span> <span class="nn">types</span></span><a href="#l2100"></a>
<span id="l2101">        <span class="n">m</span> <span class="o">=</span> <span class="n">types</span><span class="o">.</span><span class="n">ModuleType</span><span class="p">(</span><span class="n">name</span><span class="p">)</span></span><a href="#l2101"></a>
<span id="l2102">        <span class="n">m</span><span class="o">.</span><span class="n">__test__</span> <span class="o">=</span> <span class="n">d</span></span><a href="#l2102"></a>
<span id="l2103">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">rundoc</span><span class="p">(</span><span class="n">m</span><span class="p">,</span> <span class="n">name</span><span class="p">)</span></span><a href="#l2103"></a>
<span id="l2104"></span><a href="#l2104"></a>
<span id="l2105">    <span class="k">def</span> <span class="nf">summarize</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">verbose</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l2105"></a>
<span id="l2106">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">testrunner</span><span class="o">.</span><span class="n">summarize</span><span class="p">(</span><span class="n">verbose</span><span class="p">)</span></span><a href="#l2106"></a>
<span id="l2107"></span><a href="#l2107"></a>
<span id="l2108">    <span class="k">def</span> <span class="nf">merge</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l2108"></a>
<span id="l2109">        <span class="bp">self</span><span class="o">.</span><span class="n">testrunner</span><span class="o">.</span><span class="n">merge</span><span class="p">(</span><span class="n">other</span><span class="o">.</span><span class="n">testrunner</span><span class="p">)</span></span><a href="#l2109"></a>
<span id="l2110"></span><a href="#l2110"></a>
<span id="l2111"><span class="c">######################################################################</span></span><a href="#l2111"></a>
<span id="l2112"><span class="c">## 8. Unittest Support</span></span><a href="#l2112"></a>
<span id="l2113"><span class="c">######################################################################</span></span><a href="#l2113"></a>
<span id="l2114"></span><a href="#l2114"></a>
<span id="l2115"><span class="n">_unittest_reportflags</span> <span class="o">=</span> <span class="mi">0</span></span><a href="#l2115"></a>
<span id="l2116"></span><a href="#l2116"></a>
<span id="l2117"><span class="k">def</span> <span class="nf">set_unittest_reportflags</span><span class="p">(</span><span class="n">flags</span><span class="p">):</span></span><a href="#l2117"></a>
<span id="l2118">    <span class="sd">&quot;&quot;&quot;Sets the unittest option flags.</span></span><a href="#l2118"></a>
<span id="l2119"></span><a href="#l2119"></a>
<span id="l2120"><span class="sd">    The old flag is returned so that a runner could restore the old</span></span><a href="#l2120"></a>
<span id="l2121"><span class="sd">    value if it wished to:</span></span><a href="#l2121"></a>
<span id="l2122"></span><a href="#l2122"></a>
<span id="l2123"><span class="sd">      &gt;&gt;&gt; import doctest</span></span><a href="#l2123"></a>
<span id="l2124"><span class="sd">      &gt;&gt;&gt; old = doctest._unittest_reportflags</span></span><a href="#l2124"></a>
<span id="l2125"><span class="sd">      &gt;&gt;&gt; doctest.set_unittest_reportflags(REPORT_NDIFF |</span></span><a href="#l2125"></a>
<span id="l2126"><span class="sd">      ...                          REPORT_ONLY_FIRST_FAILURE) == old</span></span><a href="#l2126"></a>
<span id="l2127"><span class="sd">      True</span></span><a href="#l2127"></a>
<span id="l2128"></span><a href="#l2128"></a>
<span id="l2129"><span class="sd">      &gt;&gt;&gt; doctest._unittest_reportflags == (REPORT_NDIFF |</span></span><a href="#l2129"></a>
<span id="l2130"><span class="sd">      ...                                   REPORT_ONLY_FIRST_FAILURE)</span></span><a href="#l2130"></a>
<span id="l2131"><span class="sd">      True</span></span><a href="#l2131"></a>
<span id="l2132"></span><a href="#l2132"></a>
<span id="l2133"><span class="sd">    Only reporting flags can be set:</span></span><a href="#l2133"></a>
<span id="l2134"></span><a href="#l2134"></a>
<span id="l2135"><span class="sd">      &gt;&gt;&gt; doctest.set_unittest_reportflags(ELLIPSIS)</span></span><a href="#l2135"></a>
<span id="l2136"><span class="sd">      Traceback (most recent call last):</span></span><a href="#l2136"></a>
<span id="l2137"><span class="sd">      ...</span></span><a href="#l2137"></a>
<span id="l2138"><span class="sd">      ValueError: (&#39;Only reporting flags allowed&#39;, 8)</span></span><a href="#l2138"></a>
<span id="l2139"></span><a href="#l2139"></a>
<span id="l2140"><span class="sd">      &gt;&gt;&gt; doctest.set_unittest_reportflags(old) == (REPORT_NDIFF |</span></span><a href="#l2140"></a>
<span id="l2141"><span class="sd">      ...                                   REPORT_ONLY_FIRST_FAILURE)</span></span><a href="#l2141"></a>
<span id="l2142"><span class="sd">      True</span></span><a href="#l2142"></a>
<span id="l2143"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l2143"></a>
<span id="l2144">    <span class="k">global</span> <span class="n">_unittest_reportflags</span></span><a href="#l2144"></a>
<span id="l2145"></span><a href="#l2145"></a>
<span id="l2146">    <span class="k">if</span> <span class="p">(</span><span class="n">flags</span> <span class="o">&amp;</span> <span class="n">REPORTING_FLAGS</span><span class="p">)</span> <span class="o">!=</span> <span class="n">flags</span><span class="p">:</span></span><a href="#l2146"></a>
<span id="l2147">        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&quot;Only reporting flags allowed&quot;</span><span class="p">,</span> <span class="n">flags</span><span class="p">)</span></span><a href="#l2147"></a>
<span id="l2148">    <span class="n">old</span> <span class="o">=</span> <span class="n">_unittest_reportflags</span></span><a href="#l2148"></a>
<span id="l2149">    <span class="n">_unittest_reportflags</span> <span class="o">=</span> <span class="n">flags</span></span><a href="#l2149"></a>
<span id="l2150">    <span class="k">return</span> <span class="n">old</span></span><a href="#l2150"></a>
<span id="l2151"></span><a href="#l2151"></a>
<span id="l2152"></span><a href="#l2152"></a>
<span id="l2153"><span class="k">class</span> <span class="nc">DocTestCase</span><span class="p">(</span><span class="n">unittest</span><span class="o">.</span><span class="n">TestCase</span><span class="p">):</span></span><a href="#l2153"></a>
<span id="l2154"></span><a href="#l2154"></a>
<span id="l2155">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">test</span><span class="p">,</span> <span class="n">optionflags</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">setUp</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">tearDown</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></span><a href="#l2155"></a>
<span id="l2156">                 <span class="n">checker</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l2156"></a>
<span id="l2157"></span><a href="#l2157"></a>
<span id="l2158">        <span class="n">unittest</span><span class="o">.</span><span class="n">TestCase</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span></span><a href="#l2158"></a>
<span id="l2159">        <span class="bp">self</span><span class="o">.</span><span class="n">_dt_optionflags</span> <span class="o">=</span> <span class="n">optionflags</span></span><a href="#l2159"></a>
<span id="l2160">        <span class="bp">self</span><span class="o">.</span><span class="n">_dt_checker</span> <span class="o">=</span> <span class="n">checker</span></span><a href="#l2160"></a>
<span id="l2161">        <span class="bp">self</span><span class="o">.</span><span class="n">_dt_test</span> <span class="o">=</span> <span class="n">test</span></span><a href="#l2161"></a>
<span id="l2162">        <span class="bp">self</span><span class="o">.</span><span class="n">_dt_setUp</span> <span class="o">=</span> <span class="n">setUp</span></span><a href="#l2162"></a>
<span id="l2163">        <span class="bp">self</span><span class="o">.</span><span class="n">_dt_tearDown</span> <span class="o">=</span> <span class="n">tearDown</span></span><a href="#l2163"></a>
<span id="l2164"></span><a href="#l2164"></a>
<span id="l2165">    <span class="k">def</span> <span class="nf">setUp</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l2165"></a>
<span id="l2166">        <span class="n">test</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_dt_test</span></span><a href="#l2166"></a>
<span id="l2167"></span><a href="#l2167"></a>
<span id="l2168">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_dt_setUp</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l2168"></a>
<span id="l2169">            <span class="bp">self</span><span class="o">.</span><span class="n">_dt_setUp</span><span class="p">(</span><span class="n">test</span><span class="p">)</span></span><a href="#l2169"></a>
<span id="l2170"></span><a href="#l2170"></a>
<span id="l2171">    <span class="k">def</span> <span class="nf">tearDown</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l2171"></a>
<span id="l2172">        <span class="n">test</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_dt_test</span></span><a href="#l2172"></a>
<span id="l2173"></span><a href="#l2173"></a>
<span id="l2174">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_dt_tearDown</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l2174"></a>
<span id="l2175">            <span class="bp">self</span><span class="o">.</span><span class="n">_dt_tearDown</span><span class="p">(</span><span class="n">test</span><span class="p">)</span></span><a href="#l2175"></a>
<span id="l2176"></span><a href="#l2176"></a>
<span id="l2177">        <span class="n">test</span><span class="o">.</span><span class="n">globs</span><span class="o">.</span><span class="n">clear</span><span class="p">()</span></span><a href="#l2177"></a>
<span id="l2178"></span><a href="#l2178"></a>
<span id="l2179">    <span class="k">def</span> <span class="nf">runTest</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l2179"></a>
<span id="l2180">        <span class="n">test</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_dt_test</span></span><a href="#l2180"></a>
<span id="l2181">        <span class="n">old</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">stdout</span></span><a href="#l2181"></a>
<span id="l2182">        <span class="n">new</span> <span class="o">=</span> <span class="n">StringIO</span><span class="p">()</span></span><a href="#l2182"></a>
<span id="l2183">        <span class="n">optionflags</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_dt_optionflags</span></span><a href="#l2183"></a>
<span id="l2184"></span><a href="#l2184"></a>
<span id="l2185">        <span class="k">if</span> <span class="ow">not</span> <span class="p">(</span><span class="n">optionflags</span> <span class="o">&amp;</span> <span class="n">REPORTING_FLAGS</span><span class="p">):</span></span><a href="#l2185"></a>
<span id="l2186">            <span class="c"># The option flags don&#39;t include any reporting flags,</span></span><a href="#l2186"></a>
<span id="l2187">            <span class="c"># so add the default reporting flags</span></span><a href="#l2187"></a>
<span id="l2188">            <span class="n">optionflags</span> <span class="o">|=</span> <span class="n">_unittest_reportflags</span></span><a href="#l2188"></a>
<span id="l2189"></span><a href="#l2189"></a>
<span id="l2190">        <span class="n">runner</span> <span class="o">=</span> <span class="n">DocTestRunner</span><span class="p">(</span><span class="n">optionflags</span><span class="o">=</span><span class="n">optionflags</span><span class="p">,</span></span><a href="#l2190"></a>
<span id="l2191">                               <span class="n">checker</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_dt_checker</span><span class="p">,</span> <span class="n">verbose</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span></span><a href="#l2191"></a>
<span id="l2192"></span><a href="#l2192"></a>
<span id="l2193">        <span class="k">try</span><span class="p">:</span></span><a href="#l2193"></a>
<span id="l2194">            <span class="n">runner</span><span class="o">.</span><span class="n">DIVIDER</span> <span class="o">=</span> <span class="s">&quot;-&quot;</span><span class="o">*</span><span class="mi">70</span></span><a href="#l2194"></a>
<span id="l2195">            <span class="n">failures</span><span class="p">,</span> <span class="n">tries</span> <span class="o">=</span> <span class="n">runner</span><span class="o">.</span><span class="n">run</span><span class="p">(</span></span><a href="#l2195"></a>
<span id="l2196">                <span class="n">test</span><span class="p">,</span> <span class="n">out</span><span class="o">=</span><span class="n">new</span><span class="o">.</span><span class="n">write</span><span class="p">,</span> <span class="n">clear_globs</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span></span><a href="#l2196"></a>
<span id="l2197">        <span class="k">finally</span><span class="p">:</span></span><a href="#l2197"></a>
<span id="l2198">            <span class="n">sys</span><span class="o">.</span><span class="n">stdout</span> <span class="o">=</span> <span class="n">old</span></span><a href="#l2198"></a>
<span id="l2199"></span><a href="#l2199"></a>
<span id="l2200">        <span class="k">if</span> <span class="n">failures</span><span class="p">:</span></span><a href="#l2200"></a>
<span id="l2201">            <span class="k">raise</span> <span class="bp">self</span><span class="o">.</span><span class="n">failureException</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">format_failure</span><span class="p">(</span><span class="n">new</span><span class="o">.</span><span class="n">getvalue</span><span class="p">()))</span></span><a href="#l2201"></a>
<span id="l2202"></span><a href="#l2202"></a>
<span id="l2203">    <span class="k">def</span> <span class="nf">format_failure</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">err</span><span class="p">):</span></span><a href="#l2203"></a>
<span id="l2204">        <span class="n">test</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_dt_test</span></span><a href="#l2204"></a>
<span id="l2205">        <span class="k">if</span> <span class="n">test</span><span class="o">.</span><span class="n">lineno</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l2205"></a>
<span id="l2206">            <span class="n">lineno</span> <span class="o">=</span> <span class="s">&#39;unknown line number&#39;</span></span><a href="#l2206"></a>
<span id="l2207">        <span class="k">else</span><span class="p">:</span></span><a href="#l2207"></a>
<span id="l2208">            <span class="n">lineno</span> <span class="o">=</span> <span class="s">&#39;</span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">test</span><span class="o">.</span><span class="n">lineno</span></span><a href="#l2208"></a>
<span id="l2209">        <span class="n">lname</span> <span class="o">=</span> <span class="s">&#39;.&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">test</span><span class="o">.</span><span class="n">name</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;.&#39;</span><span class="p">)[</span><span class="o">-</span><span class="mi">1</span><span class="p">:])</span></span><a href="#l2209"></a>
<span id="l2210">        <span class="k">return</span> <span class="p">(</span><span class="s">&#39;Failed doctest test for </span><span class="si">%s</span><span class="se">\n</span><span class="s">&#39;</span></span><a href="#l2210"></a>
<span id="l2211">                <span class="s">&#39;  File &quot;</span><span class="si">%s</span><span class="s">&quot;, line </span><span class="si">%s</span><span class="s">, in </span><span class="si">%s</span><span class="se">\n\n</span><span class="si">%s</span><span class="s">&#39;</span></span><a href="#l2211"></a>
<span id="l2212">                <span class="o">%</span> <span class="p">(</span><span class="n">test</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="n">test</span><span class="o">.</span><span class="n">filename</span><span class="p">,</span> <span class="n">lineno</span><span class="p">,</span> <span class="n">lname</span><span class="p">,</span> <span class="n">err</span><span class="p">)</span></span><a href="#l2212"></a>
<span id="l2213">                <span class="p">)</span></span><a href="#l2213"></a>
<span id="l2214"></span><a href="#l2214"></a>
<span id="l2215">    <span class="k">def</span> <span class="nf">debug</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l2215"></a>
<span id="l2216">        <span class="sd">r&quot;&quot;&quot;Run the test case without results and without catching exceptions</span></span><a href="#l2216"></a>
<span id="l2217"></span><a href="#l2217"></a>
<span id="l2218"><span class="sd">           The unit test framework includes a debug method on test cases</span></span><a href="#l2218"></a>
<span id="l2219"><span class="sd">           and test suites to support post-mortem debugging.  The test code</span></span><a href="#l2219"></a>
<span id="l2220"><span class="sd">           is run in such a way that errors are not caught.  This way a</span></span><a href="#l2220"></a>
<span id="l2221"><span class="sd">           caller can catch the errors and initiate post-mortem debugging.</span></span><a href="#l2221"></a>
<span id="l2222"></span><a href="#l2222"></a>
<span id="l2223"><span class="sd">           The DocTestCase provides a debug method that raises</span></span><a href="#l2223"></a>
<span id="l2224"><span class="sd">           UnexpectedException errors if there is an unexpected</span></span><a href="#l2224"></a>
<span id="l2225"><span class="sd">           exception:</span></span><a href="#l2225"></a>
<span id="l2226"></span><a href="#l2226"></a>
<span id="l2227"><span class="sd">             &gt;&gt;&gt; test = DocTestParser().get_doctest(&#39;&gt;&gt;&gt; raise KeyError\n42&#39;,</span></span><a href="#l2227"></a>
<span id="l2228"><span class="sd">             ...                {}, &#39;foo&#39;, &#39;foo.py&#39;, 0)</span></span><a href="#l2228"></a>
<span id="l2229"><span class="sd">             &gt;&gt;&gt; case = DocTestCase(test)</span></span><a href="#l2229"></a>
<span id="l2230"><span class="sd">             &gt;&gt;&gt; try:</span></span><a href="#l2230"></a>
<span id="l2231"><span class="sd">             ...     case.debug()</span></span><a href="#l2231"></a>
<span id="l2232"><span class="sd">             ... except UnexpectedException, failure:</span></span><a href="#l2232"></a>
<span id="l2233"><span class="sd">             ...     pass</span></span><a href="#l2233"></a>
<span id="l2234"></span><a href="#l2234"></a>
<span id="l2235"><span class="sd">           The UnexpectedException contains the test, the example, and</span></span><a href="#l2235"></a>
<span id="l2236"><span class="sd">           the original exception:</span></span><a href="#l2236"></a>
<span id="l2237"></span><a href="#l2237"></a>
<span id="l2238"><span class="sd">             &gt;&gt;&gt; failure.test is test</span></span><a href="#l2238"></a>
<span id="l2239"><span class="sd">             True</span></span><a href="#l2239"></a>
<span id="l2240"></span><a href="#l2240"></a>
<span id="l2241"><span class="sd">             &gt;&gt;&gt; failure.example.want</span></span><a href="#l2241"></a>
<span id="l2242"><span class="sd">             &#39;42\n&#39;</span></span><a href="#l2242"></a>
<span id="l2243"></span><a href="#l2243"></a>
<span id="l2244"><span class="sd">             &gt;&gt;&gt; exc_info = failure.exc_info</span></span><a href="#l2244"></a>
<span id="l2245"><span class="sd">             &gt;&gt;&gt; raise exc_info[0], exc_info[1], exc_info[2]</span></span><a href="#l2245"></a>
<span id="l2246"><span class="sd">             Traceback (most recent call last):</span></span><a href="#l2246"></a>
<span id="l2247"><span class="sd">             ...</span></span><a href="#l2247"></a>
<span id="l2248"><span class="sd">             KeyError</span></span><a href="#l2248"></a>
<span id="l2249"></span><a href="#l2249"></a>
<span id="l2250"><span class="sd">           If the output doesn&#39;t match, then a DocTestFailure is raised:</span></span><a href="#l2250"></a>
<span id="l2251"></span><a href="#l2251"></a>
<span id="l2252"><span class="sd">             &gt;&gt;&gt; test = DocTestParser().get_doctest(&#39;&#39;&#39;</span></span><a href="#l2252"></a>
<span id="l2253"><span class="sd">             ...      &gt;&gt;&gt; x = 1</span></span><a href="#l2253"></a>
<span id="l2254"><span class="sd">             ...      &gt;&gt;&gt; x</span></span><a href="#l2254"></a>
<span id="l2255"><span class="sd">             ...      2</span></span><a href="#l2255"></a>
<span id="l2256"><span class="sd">             ...      &#39;&#39;&#39;, {}, &#39;foo&#39;, &#39;foo.py&#39;, 0)</span></span><a href="#l2256"></a>
<span id="l2257"><span class="sd">             &gt;&gt;&gt; case = DocTestCase(test)</span></span><a href="#l2257"></a>
<span id="l2258"></span><a href="#l2258"></a>
<span id="l2259"><span class="sd">             &gt;&gt;&gt; try:</span></span><a href="#l2259"></a>
<span id="l2260"><span class="sd">             ...    case.debug()</span></span><a href="#l2260"></a>
<span id="l2261"><span class="sd">             ... except DocTestFailure, failure:</span></span><a href="#l2261"></a>
<span id="l2262"><span class="sd">             ...    pass</span></span><a href="#l2262"></a>
<span id="l2263"></span><a href="#l2263"></a>
<span id="l2264"><span class="sd">           DocTestFailure objects provide access to the test:</span></span><a href="#l2264"></a>
<span id="l2265"></span><a href="#l2265"></a>
<span id="l2266"><span class="sd">             &gt;&gt;&gt; failure.test is test</span></span><a href="#l2266"></a>
<span id="l2267"><span class="sd">             True</span></span><a href="#l2267"></a>
<span id="l2268"></span><a href="#l2268"></a>
<span id="l2269"><span class="sd">           As well as to the example:</span></span><a href="#l2269"></a>
<span id="l2270"></span><a href="#l2270"></a>
<span id="l2271"><span class="sd">             &gt;&gt;&gt; failure.example.want</span></span><a href="#l2271"></a>
<span id="l2272"><span class="sd">             &#39;2\n&#39;</span></span><a href="#l2272"></a>
<span id="l2273"></span><a href="#l2273"></a>
<span id="l2274"><span class="sd">           and the actual output:</span></span><a href="#l2274"></a>
<span id="l2275"></span><a href="#l2275"></a>
<span id="l2276"><span class="sd">             &gt;&gt;&gt; failure.got</span></span><a href="#l2276"></a>
<span id="l2277"><span class="sd">             &#39;1\n&#39;</span></span><a href="#l2277"></a>
<span id="l2278"></span><a href="#l2278"></a>
<span id="l2279"><span class="sd">           &quot;&quot;&quot;</span></span><a href="#l2279"></a>
<span id="l2280"></span><a href="#l2280"></a>
<span id="l2281">        <span class="bp">self</span><span class="o">.</span><span class="n">setUp</span><span class="p">()</span></span><a href="#l2281"></a>
<span id="l2282">        <span class="n">runner</span> <span class="o">=</span> <span class="n">DebugRunner</span><span class="p">(</span><span class="n">optionflags</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_dt_optionflags</span><span class="p">,</span></span><a href="#l2282"></a>
<span id="l2283">                             <span class="n">checker</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_dt_checker</span><span class="p">,</span> <span class="n">verbose</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span></span><a href="#l2283"></a>
<span id="l2284">        <span class="n">runner</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_dt_test</span><span class="p">,</span> <span class="n">clear_globs</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span></span><a href="#l2284"></a>
<span id="l2285">        <span class="bp">self</span><span class="o">.</span><span class="n">tearDown</span><span class="p">()</span></span><a href="#l2285"></a>
<span id="l2286"></span><a href="#l2286"></a>
<span id="l2287">    <span class="k">def</span> <span class="nf">id</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l2287"></a>
<span id="l2288">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_dt_test</span><span class="o">.</span><span class="n">name</span></span><a href="#l2288"></a>
<span id="l2289"></span><a href="#l2289"></a>
<span id="l2290">    <span class="k">def</span> <span class="nf">__eq__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l2290"></a>
<span id="l2291">        <span class="k">if</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="ow">is</span> <span class="ow">not</span> <span class="nb">type</span><span class="p">(</span><span class="n">other</span><span class="p">):</span></span><a href="#l2291"></a>
<span id="l2292">            <span class="k">return</span> <span class="bp">NotImplemented</span></span><a href="#l2292"></a>
<span id="l2293"></span><a href="#l2293"></a>
<span id="l2294">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_dt_test</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">_dt_test</span> <span class="ow">and</span> \</span><a href="#l2294"></a>
<span id="l2295">               <span class="bp">self</span><span class="o">.</span><span class="n">_dt_optionflags</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">_dt_optionflags</span> <span class="ow">and</span> \</span><a href="#l2295"></a>
<span id="l2296">               <span class="bp">self</span><span class="o">.</span><span class="n">_dt_setUp</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">_dt_setUp</span> <span class="ow">and</span> \</span><a href="#l2296"></a>
<span id="l2297">               <span class="bp">self</span><span class="o">.</span><span class="n">_dt_tearDown</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">_dt_tearDown</span> <span class="ow">and</span> \</span><a href="#l2297"></a>
<span id="l2298">               <span class="bp">self</span><span class="o">.</span><span class="n">_dt_checker</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">_dt_checker</span></span><a href="#l2298"></a>
<span id="l2299"></span><a href="#l2299"></a>
<span id="l2300">    <span class="k">def</span> <span class="nf">__ne__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l2300"></a>
<span id="l2301">        <span class="k">return</span> <span class="ow">not</span> <span class="bp">self</span> <span class="o">==</span> <span class="n">other</span></span><a href="#l2301"></a>
<span id="l2302"></span><a href="#l2302"></a>
<span id="l2303">    <span class="k">def</span> <span class="nf">__hash__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l2303"></a>
<span id="l2304">        <span class="k">return</span> <span class="nb">hash</span><span class="p">((</span><span class="bp">self</span><span class="o">.</span><span class="n">_dt_optionflags</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_dt_setUp</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_dt_tearDown</span><span class="p">,</span></span><a href="#l2304"></a>
<span id="l2305">                     <span class="bp">self</span><span class="o">.</span><span class="n">_dt_checker</span><span class="p">))</span></span><a href="#l2305"></a>
<span id="l2306"></span><a href="#l2306"></a>
<span id="l2307">    <span class="k">def</span> <span class="nf">__repr__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l2307"></a>
<span id="l2308">        <span class="n">name</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_dt_test</span><span class="o">.</span><span class="n">name</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;.&#39;</span><span class="p">)</span></span><a href="#l2308"></a>
<span id="l2309">        <span class="k">return</span> <span class="s">&quot;</span><span class="si">%s</span><span class="s"> (</span><span class="si">%s</span><span class="s">)&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">name</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">],</span> <span class="s">&#39;.&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">name</span><span class="p">[:</span><span class="o">-</span><span class="mi">1</span><span class="p">]))</span></span><a href="#l2309"></a>
<span id="l2310"></span><a href="#l2310"></a>
<span id="l2311">    <span class="n">__str__</span> <span class="o">=</span> <span class="n">__repr__</span></span><a href="#l2311"></a>
<span id="l2312"></span><a href="#l2312"></a>
<span id="l2313">    <span class="k">def</span> <span class="nf">shortDescription</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l2313"></a>
<span id="l2314">        <span class="k">return</span> <span class="s">&quot;Doctest: &quot;</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">_dt_test</span><span class="o">.</span><span class="n">name</span></span><a href="#l2314"></a>
<span id="l2315"></span><a href="#l2315"></a>
<span id="l2316"><span class="k">class</span> <span class="nc">SkipDocTestCase</span><span class="p">(</span><span class="n">DocTestCase</span><span class="p">):</span></span><a href="#l2316"></a>
<span id="l2317">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l2317"></a>
<span id="l2318">        <span class="n">DocTestCase</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="bp">None</span><span class="p">)</span></span><a href="#l2318"></a>
<span id="l2319"></span><a href="#l2319"></a>
<span id="l2320">    <span class="k">def</span> <span class="nf">setUp</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l2320"></a>
<span id="l2321">        <span class="bp">self</span><span class="o">.</span><span class="n">skipTest</span><span class="p">(</span><span class="s">&quot;DocTestSuite will not work with -O2 and above&quot;</span><span class="p">)</span></span><a href="#l2321"></a>
<span id="l2322"></span><a href="#l2322"></a>
<span id="l2323">    <span class="k">def</span> <span class="nf">test_skip</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l2323"></a>
<span id="l2324">        <span class="k">pass</span></span><a href="#l2324"></a>
<span id="l2325"></span><a href="#l2325"></a>
<span id="l2326">    <span class="k">def</span> <span class="nf">shortDescription</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l2326"></a>
<span id="l2327">        <span class="k">return</span> <span class="s">&quot;Skipping tests from </span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="n">module</span><span class="o">.</span><span class="n">__name__</span></span><a href="#l2327"></a>
<span id="l2328"></span><a href="#l2328"></a>
<span id="l2329"><span class="k">def</span> <span class="nf">DocTestSuite</span><span class="p">(</span><span class="n">module</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">globs</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">extraglobs</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">test_finder</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></span><a href="#l2329"></a>
<span id="l2330">                 <span class="o">**</span><span class="n">options</span><span class="p">):</span></span><a href="#l2330"></a>
<span id="l2331">    <span class="sd">&quot;&quot;&quot;</span></span><a href="#l2331"></a>
<span id="l2332"><span class="sd">    Convert doctest tests for a module to a unittest test suite.</span></span><a href="#l2332"></a>
<span id="l2333"></span><a href="#l2333"></a>
<span id="l2334"><span class="sd">    This converts each documentation string in a module that</span></span><a href="#l2334"></a>
<span id="l2335"><span class="sd">    contains doctest tests to a unittest test case.  If any of the</span></span><a href="#l2335"></a>
<span id="l2336"><span class="sd">    tests in a doc string fail, then the test case fails.  An exception</span></span><a href="#l2336"></a>
<span id="l2337"><span class="sd">    is raised showing the name of the file containing the test and a</span></span><a href="#l2337"></a>
<span id="l2338"><span class="sd">    (sometimes approximate) line number.</span></span><a href="#l2338"></a>
<span id="l2339"></span><a href="#l2339"></a>
<span id="l2340"><span class="sd">    The `module` argument provides the module to be tested.  The argument</span></span><a href="#l2340"></a>
<span id="l2341"><span class="sd">    can be either a module or a module name.</span></span><a href="#l2341"></a>
<span id="l2342"></span><a href="#l2342"></a>
<span id="l2343"><span class="sd">    If no argument is given, the calling module is used.</span></span><a href="#l2343"></a>
<span id="l2344"></span><a href="#l2344"></a>
<span id="l2345"><span class="sd">    A number of options may be provided as keyword arguments:</span></span><a href="#l2345"></a>
<span id="l2346"></span><a href="#l2346"></a>
<span id="l2347"><span class="sd">    setUp</span></span><a href="#l2347"></a>
<span id="l2348"><span class="sd">      A set-up function.  This is called before running the</span></span><a href="#l2348"></a>
<span id="l2349"><span class="sd">      tests in each file. The setUp function will be passed a DocTest</span></span><a href="#l2349"></a>
<span id="l2350"><span class="sd">      object.  The setUp function can access the test globals as the</span></span><a href="#l2350"></a>
<span id="l2351"><span class="sd">      globs attribute of the test passed.</span></span><a href="#l2351"></a>
<span id="l2352"></span><a href="#l2352"></a>
<span id="l2353"><span class="sd">    tearDown</span></span><a href="#l2353"></a>
<span id="l2354"><span class="sd">      A tear-down function.  This is called after running the</span></span><a href="#l2354"></a>
<span id="l2355"><span class="sd">      tests in each file.  The tearDown function will be passed a DocTest</span></span><a href="#l2355"></a>
<span id="l2356"><span class="sd">      object.  The tearDown function can access the test globals as the</span></span><a href="#l2356"></a>
<span id="l2357"><span class="sd">      globs attribute of the test passed.</span></span><a href="#l2357"></a>
<span id="l2358"></span><a href="#l2358"></a>
<span id="l2359"><span class="sd">    globs</span></span><a href="#l2359"></a>
<span id="l2360"><span class="sd">      A dictionary containing initial global variables for the tests.</span></span><a href="#l2360"></a>
<span id="l2361"></span><a href="#l2361"></a>
<span id="l2362"><span class="sd">    optionflags</span></span><a href="#l2362"></a>
<span id="l2363"><span class="sd">       A set of doctest option flags expressed as an integer.</span></span><a href="#l2363"></a>
<span id="l2364"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l2364"></a>
<span id="l2365"></span><a href="#l2365"></a>
<span id="l2366">    <span class="k">if</span> <span class="n">test_finder</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l2366"></a>
<span id="l2367">        <span class="n">test_finder</span> <span class="o">=</span> <span class="n">DocTestFinder</span><span class="p">()</span></span><a href="#l2367"></a>
<span id="l2368"></span><a href="#l2368"></a>
<span id="l2369">    <span class="n">module</span> <span class="o">=</span> <span class="n">_normalize_module</span><span class="p">(</span><span class="n">module</span><span class="p">)</span></span><a href="#l2369"></a>
<span id="l2370">    <span class="n">tests</span> <span class="o">=</span> <span class="n">test_finder</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="n">module</span><span class="p">,</span> <span class="n">globs</span><span class="o">=</span><span class="n">globs</span><span class="p">,</span> <span class="n">extraglobs</span><span class="o">=</span><span class="n">extraglobs</span><span class="p">)</span></span><a href="#l2370"></a>
<span id="l2371"></span><a href="#l2371"></a>
<span id="l2372">    <span class="k">if</span> <span class="ow">not</span> <span class="n">tests</span> <span class="ow">and</span> <span class="n">sys</span><span class="o">.</span><span class="n">flags</span><span class="o">.</span><span class="n">optimize</span> <span class="o">&gt;=</span><span class="mi">2</span><span class="p">:</span></span><a href="#l2372"></a>
<span id="l2373">        <span class="c"># Skip doctests when running with -O2</span></span><a href="#l2373"></a>
<span id="l2374">        <span class="n">suite</span> <span class="o">=</span> <span class="n">unittest</span><span class="o">.</span><span class="n">TestSuite</span><span class="p">()</span></span><a href="#l2374"></a>
<span id="l2375">        <span class="n">suite</span><span class="o">.</span><span class="n">addTest</span><span class="p">(</span><span class="n">SkipDocTestCase</span><span class="p">())</span></span><a href="#l2375"></a>
<span id="l2376">        <span class="k">return</span> <span class="n">suite</span></span><a href="#l2376"></a>
<span id="l2377">    <span class="k">elif</span> <span class="ow">not</span> <span class="n">tests</span><span class="p">:</span></span><a href="#l2377"></a>
<span id="l2378">        <span class="c"># Why do we want to do this? Because it reveals a bug that might</span></span><a href="#l2378"></a>
<span id="l2379">        <span class="c"># otherwise be hidden.</span></span><a href="#l2379"></a>
<span id="l2380">        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="n">module</span><span class="p">,</span> <span class="s">&quot;has no tests&quot;</span><span class="p">)</span></span><a href="#l2380"></a>
<span id="l2381"></span><a href="#l2381"></a>
<span id="l2382">    <span class="n">tests</span><span class="o">.</span><span class="n">sort</span><span class="p">()</span></span><a href="#l2382"></a>
<span id="l2383">    <span class="n">suite</span> <span class="o">=</span> <span class="n">unittest</span><span class="o">.</span><span class="n">TestSuite</span><span class="p">()</span></span><a href="#l2383"></a>
<span id="l2384"></span><a href="#l2384"></a>
<span id="l2385">    <span class="k">for</span> <span class="n">test</span> <span class="ow">in</span> <span class="n">tests</span><span class="p">:</span></span><a href="#l2385"></a>
<span id="l2386">        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">test</span><span class="o">.</span><span class="n">examples</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span></span><a href="#l2386"></a>
<span id="l2387">            <span class="k">continue</span></span><a href="#l2387"></a>
<span id="l2388">        <span class="k">if</span> <span class="ow">not</span> <span class="n">test</span><span class="o">.</span><span class="n">filename</span><span class="p">:</span></span><a href="#l2388"></a>
<span id="l2389">            <span class="n">filename</span> <span class="o">=</span> <span class="n">module</span><span class="o">.</span><span class="n">__file__</span></span><a href="#l2389"></a>
<span id="l2390">            <span class="k">if</span> <span class="n">filename</span><span class="p">[</span><span class="o">-</span><span class="mi">4</span><span class="p">:]</span> <span class="ow">in</span> <span class="p">(</span><span class="s">&quot;.pyc&quot;</span><span class="p">,</span> <span class="s">&quot;.pyo&quot;</span><span class="p">):</span></span><a href="#l2390"></a>
<span id="l2391">                <span class="n">filename</span> <span class="o">=</span> <span class="n">filename</span><span class="p">[:</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span></span><a href="#l2391"></a>
<span id="l2392">            <span class="n">test</span><span class="o">.</span><span class="n">filename</span> <span class="o">=</span> <span class="n">filename</span></span><a href="#l2392"></a>
<span id="l2393">        <span class="n">suite</span><span class="o">.</span><span class="n">addTest</span><span class="p">(</span><span class="n">DocTestCase</span><span class="p">(</span><span class="n">test</span><span class="p">,</span> <span class="o">**</span><span class="n">options</span><span class="p">))</span></span><a href="#l2393"></a>
<span id="l2394"></span><a href="#l2394"></a>
<span id="l2395">    <span class="k">return</span> <span class="n">suite</span></span><a href="#l2395"></a>
<span id="l2396"></span><a href="#l2396"></a>
<span id="l2397"><span class="k">class</span> <span class="nc">DocFileCase</span><span class="p">(</span><span class="n">DocTestCase</span><span class="p">):</span></span><a href="#l2397"></a>
<span id="l2398"></span><a href="#l2398"></a>
<span id="l2399">    <span class="k">def</span> <span class="nf">id</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l2399"></a>
<span id="l2400">        <span class="k">return</span> <span class="s">&#39;_&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_dt_test</span><span class="o">.</span><span class="n">name</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;.&#39;</span><span class="p">))</span></span><a href="#l2400"></a>
<span id="l2401"></span><a href="#l2401"></a>
<span id="l2402">    <span class="k">def</span> <span class="nf">__repr__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l2402"></a>
<span id="l2403">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_dt_test</span><span class="o">.</span><span class="n">filename</span></span><a href="#l2403"></a>
<span id="l2404">    <span class="n">__str__</span> <span class="o">=</span> <span class="n">__repr__</span></span><a href="#l2404"></a>
<span id="l2405"></span><a href="#l2405"></a>
<span id="l2406">    <span class="k">def</span> <span class="nf">format_failure</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">err</span><span class="p">):</span></span><a href="#l2406"></a>
<span id="l2407">        <span class="k">return</span> <span class="p">(</span><span class="s">&#39;Failed doctest test for </span><span class="si">%s</span><span class="se">\n</span><span class="s">  File &quot;</span><span class="si">%s</span><span class="s">&quot;, line 0</span><span class="se">\n\n</span><span class="si">%s</span><span class="s">&#39;</span></span><a href="#l2407"></a>
<span id="l2408">                <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_dt_test</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_dt_test</span><span class="o">.</span><span class="n">filename</span><span class="p">,</span> <span class="n">err</span><span class="p">)</span></span><a href="#l2408"></a>
<span id="l2409">                <span class="p">)</span></span><a href="#l2409"></a>
<span id="l2410"></span><a href="#l2410"></a>
<span id="l2411"><span class="k">def</span> <span class="nf">DocFileTest</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="n">module_relative</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span> <span class="n">package</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></span><a href="#l2411"></a>
<span id="l2412">                <span class="n">globs</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">parser</span><span class="o">=</span><span class="n">DocTestParser</span><span class="p">(),</span></span><a href="#l2412"></a>
<span id="l2413">                <span class="n">encoding</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="o">**</span><span class="n">options</span><span class="p">):</span></span><a href="#l2413"></a>
<span id="l2414">    <span class="k">if</span> <span class="n">globs</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l2414"></a>
<span id="l2415">        <span class="n">globs</span> <span class="o">=</span> <span class="p">{}</span></span><a href="#l2415"></a>
<span id="l2416">    <span class="k">else</span><span class="p">:</span></span><a href="#l2416"></a>
<span id="l2417">        <span class="n">globs</span> <span class="o">=</span> <span class="n">globs</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span></span><a href="#l2417"></a>
<span id="l2418"></span><a href="#l2418"></a>
<span id="l2419">    <span class="k">if</span> <span class="n">package</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">module_relative</span><span class="p">:</span></span><a href="#l2419"></a>
<span id="l2420">        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&quot;Package may only be specified for module-&quot;</span></span><a href="#l2420"></a>
<span id="l2421">                         <span class="s">&quot;relative paths.&quot;</span><span class="p">)</span></span><a href="#l2421"></a>
<span id="l2422"></span><a href="#l2422"></a>
<span id="l2423">    <span class="c"># Relativize the path.</span></span><a href="#l2423"></a>
<span id="l2424">    <span class="n">doc</span><span class="p">,</span> <span class="n">path</span> <span class="o">=</span> <span class="n">_load_testfile</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="n">package</span><span class="p">,</span> <span class="n">module_relative</span><span class="p">)</span></span><a href="#l2424"></a>
<span id="l2425"></span><a href="#l2425"></a>
<span id="l2426">    <span class="k">if</span> <span class="s">&quot;__file__&quot;</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">globs</span><span class="p">:</span></span><a href="#l2426"></a>
<span id="l2427">        <span class="n">globs</span><span class="p">[</span><span class="s">&quot;__file__&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">path</span></span><a href="#l2427"></a>
<span id="l2428"></span><a href="#l2428"></a>
<span id="l2429">    <span class="c"># Find the file and read it.</span></span><a href="#l2429"></a>
<span id="l2430">    <span class="n">name</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">basename</span><span class="p">(</span><span class="n">path</span><span class="p">)</span></span><a href="#l2430"></a>
<span id="l2431"></span><a href="#l2431"></a>
<span id="l2432">    <span class="c"># If an encoding is specified, use it to convert the file to unicode</span></span><a href="#l2432"></a>
<span id="l2433">    <span class="k">if</span> <span class="n">encoding</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l2433"></a>
<span id="l2434">        <span class="n">doc</span> <span class="o">=</span> <span class="n">doc</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="n">encoding</span><span class="p">)</span></span><a href="#l2434"></a>
<span id="l2435"></span><a href="#l2435"></a>
<span id="l2436">    <span class="c"># Convert it to a test, and wrap it in a DocFileCase.</span></span><a href="#l2436"></a>
<span id="l2437">    <span class="n">test</span> <span class="o">=</span> <span class="n">parser</span><span class="o">.</span><span class="n">get_doctest</span><span class="p">(</span><span class="n">doc</span><span class="p">,</span> <span class="n">globs</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">path</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span></span><a href="#l2437"></a>
<span id="l2438">    <span class="k">return</span> <span class="n">DocFileCase</span><span class="p">(</span><span class="n">test</span><span class="p">,</span> <span class="o">**</span><span class="n">options</span><span class="p">)</span></span><a href="#l2438"></a>
<span id="l2439"></span><a href="#l2439"></a>
<span id="l2440"><span class="k">def</span> <span class="nf">DocFileSuite</span><span class="p">(</span><span class="o">*</span><span class="n">paths</span><span class="p">,</span> <span class="o">**</span><span class="n">kw</span><span class="p">):</span></span><a href="#l2440"></a>
<span id="l2441">    <span class="sd">&quot;&quot;&quot;A unittest suite for one or more doctest files.</span></span><a href="#l2441"></a>
<span id="l2442"></span><a href="#l2442"></a>
<span id="l2443"><span class="sd">    The path to each doctest file is given as a string; the</span></span><a href="#l2443"></a>
<span id="l2444"><span class="sd">    interpretation of that string depends on the keyword argument</span></span><a href="#l2444"></a>
<span id="l2445"><span class="sd">    &quot;module_relative&quot;.</span></span><a href="#l2445"></a>
<span id="l2446"></span><a href="#l2446"></a>
<span id="l2447"><span class="sd">    A number of options may be provided as keyword arguments:</span></span><a href="#l2447"></a>
<span id="l2448"></span><a href="#l2448"></a>
<span id="l2449"><span class="sd">    module_relative</span></span><a href="#l2449"></a>
<span id="l2450"><span class="sd">      If &quot;module_relative&quot; is True, then the given file paths are</span></span><a href="#l2450"></a>
<span id="l2451"><span class="sd">      interpreted as os-independent module-relative paths.  By</span></span><a href="#l2451"></a>
<span id="l2452"><span class="sd">      default, these paths are relative to the calling module&#39;s</span></span><a href="#l2452"></a>
<span id="l2453"><span class="sd">      directory; but if the &quot;package&quot; argument is specified, then</span></span><a href="#l2453"></a>
<span id="l2454"><span class="sd">      they are relative to that package.  To ensure os-independence,</span></span><a href="#l2454"></a>
<span id="l2455"><span class="sd">      &quot;filename&quot; should use &quot;/&quot; characters to separate path</span></span><a href="#l2455"></a>
<span id="l2456"><span class="sd">      segments, and may not be an absolute path (i.e., it may not</span></span><a href="#l2456"></a>
<span id="l2457"><span class="sd">      begin with &quot;/&quot;).</span></span><a href="#l2457"></a>
<span id="l2458"></span><a href="#l2458"></a>
<span id="l2459"><span class="sd">      If &quot;module_relative&quot; is False, then the given file paths are</span></span><a href="#l2459"></a>
<span id="l2460"><span class="sd">      interpreted as os-specific paths.  These paths may be absolute</span></span><a href="#l2460"></a>
<span id="l2461"><span class="sd">      or relative (to the current working directory).</span></span><a href="#l2461"></a>
<span id="l2462"></span><a href="#l2462"></a>
<span id="l2463"><span class="sd">    package</span></span><a href="#l2463"></a>
<span id="l2464"><span class="sd">      A Python package or the name of a Python package whose directory</span></span><a href="#l2464"></a>
<span id="l2465"><span class="sd">      should be used as the base directory for module relative paths.</span></span><a href="#l2465"></a>
<span id="l2466"><span class="sd">      If &quot;package&quot; is not specified, then the calling module&#39;s</span></span><a href="#l2466"></a>
<span id="l2467"><span class="sd">      directory is used as the base directory for module relative</span></span><a href="#l2467"></a>
<span id="l2468"><span class="sd">      filenames.  It is an error to specify &quot;package&quot; if</span></span><a href="#l2468"></a>
<span id="l2469"><span class="sd">      &quot;module_relative&quot; is False.</span></span><a href="#l2469"></a>
<span id="l2470"></span><a href="#l2470"></a>
<span id="l2471"><span class="sd">    setUp</span></span><a href="#l2471"></a>
<span id="l2472"><span class="sd">      A set-up function.  This is called before running the</span></span><a href="#l2472"></a>
<span id="l2473"><span class="sd">      tests in each file. The setUp function will be passed a DocTest</span></span><a href="#l2473"></a>
<span id="l2474"><span class="sd">      object.  The setUp function can access the test globals as the</span></span><a href="#l2474"></a>
<span id="l2475"><span class="sd">      globs attribute of the test passed.</span></span><a href="#l2475"></a>
<span id="l2476"></span><a href="#l2476"></a>
<span id="l2477"><span class="sd">    tearDown</span></span><a href="#l2477"></a>
<span id="l2478"><span class="sd">      A tear-down function.  This is called after running the</span></span><a href="#l2478"></a>
<span id="l2479"><span class="sd">      tests in each file.  The tearDown function will be passed a DocTest</span></span><a href="#l2479"></a>
<span id="l2480"><span class="sd">      object.  The tearDown function can access the test globals as the</span></span><a href="#l2480"></a>
<span id="l2481"><span class="sd">      globs attribute of the test passed.</span></span><a href="#l2481"></a>
<span id="l2482"></span><a href="#l2482"></a>
<span id="l2483"><span class="sd">    globs</span></span><a href="#l2483"></a>
<span id="l2484"><span class="sd">      A dictionary containing initial global variables for the tests.</span></span><a href="#l2484"></a>
<span id="l2485"></span><a href="#l2485"></a>
<span id="l2486"><span class="sd">    optionflags</span></span><a href="#l2486"></a>
<span id="l2487"><span class="sd">      A set of doctest option flags expressed as an integer.</span></span><a href="#l2487"></a>
<span id="l2488"></span><a href="#l2488"></a>
<span id="l2489"><span class="sd">    parser</span></span><a href="#l2489"></a>
<span id="l2490"><span class="sd">      A DocTestParser (or subclass) that should be used to extract</span></span><a href="#l2490"></a>
<span id="l2491"><span class="sd">      tests from the files.</span></span><a href="#l2491"></a>
<span id="l2492"></span><a href="#l2492"></a>
<span id="l2493"><span class="sd">    encoding</span></span><a href="#l2493"></a>
<span id="l2494"><span class="sd">      An encoding that will be used to convert the files to unicode.</span></span><a href="#l2494"></a>
<span id="l2495"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l2495"></a>
<span id="l2496">    <span class="n">suite</span> <span class="o">=</span> <span class="n">unittest</span><span class="o">.</span><span class="n">TestSuite</span><span class="p">()</span></span><a href="#l2496"></a>
<span id="l2497"></span><a href="#l2497"></a>
<span id="l2498">    <span class="c"># We do this here so that _normalize_module is called at the right</span></span><a href="#l2498"></a>
<span id="l2499">    <span class="c"># level.  If it were called in DocFileTest, then this function</span></span><a href="#l2499"></a>
<span id="l2500">    <span class="c"># would be the caller and we might guess the package incorrectly.</span></span><a href="#l2500"></a>
<span id="l2501">    <span class="k">if</span> <span class="n">kw</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;module_relative&#39;</span><span class="p">,</span> <span class="bp">True</span><span class="p">):</span></span><a href="#l2501"></a>
<span id="l2502">        <span class="n">kw</span><span class="p">[</span><span class="s">&#39;package&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">_normalize_module</span><span class="p">(</span><span class="n">kw</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;package&#39;</span><span class="p">))</span></span><a href="#l2502"></a>
<span id="l2503"></span><a href="#l2503"></a>
<span id="l2504">    <span class="k">for</span> <span class="n">path</span> <span class="ow">in</span> <span class="n">paths</span><span class="p">:</span></span><a href="#l2504"></a>
<span id="l2505">        <span class="n">suite</span><span class="o">.</span><span class="n">addTest</span><span class="p">(</span><span class="n">DocFileTest</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="o">**</span><span class="n">kw</span><span class="p">))</span></span><a href="#l2505"></a>
<span id="l2506"></span><a href="#l2506"></a>
<span id="l2507">    <span class="k">return</span> <span class="n">suite</span></span><a href="#l2507"></a>
<span id="l2508"></span><a href="#l2508"></a>
<span id="l2509"><span class="c">######################################################################</span></span><a href="#l2509"></a>
<span id="l2510"><span class="c">## 9. Debugging Support</span></span><a href="#l2510"></a>
<span id="l2511"><span class="c">######################################################################</span></span><a href="#l2511"></a>
<span id="l2512"></span><a href="#l2512"></a>
<span id="l2513"><span class="k">def</span> <span class="nf">script_from_examples</span><span class="p">(</span><span class="n">s</span><span class="p">):</span></span><a href="#l2513"></a>
<span id="l2514">    <span class="sd">r&quot;&quot;&quot;Extract script from text with examples.</span></span><a href="#l2514"></a>
<span id="l2515"></span><a href="#l2515"></a>
<span id="l2516"><span class="sd">       Converts text with examples to a Python script.  Example input is</span></span><a href="#l2516"></a>
<span id="l2517"><span class="sd">       converted to regular code.  Example output and all other words</span></span><a href="#l2517"></a>
<span id="l2518"><span class="sd">       are converted to comments:</span></span><a href="#l2518"></a>
<span id="l2519"></span><a href="#l2519"></a>
<span id="l2520"><span class="sd">       &gt;&gt;&gt; text = &#39;&#39;&#39;</span></span><a href="#l2520"></a>
<span id="l2521"><span class="sd">       ...       Here are examples of simple math.</span></span><a href="#l2521"></a>
<span id="l2522"><span class="sd">       ...</span></span><a href="#l2522"></a>
<span id="l2523"><span class="sd">       ...           Python has super accurate integer addition</span></span><a href="#l2523"></a>
<span id="l2524"><span class="sd">       ...</span></span><a href="#l2524"></a>
<span id="l2525"><span class="sd">       ...           &gt;&gt;&gt; 2 + 2</span></span><a href="#l2525"></a>
<span id="l2526"><span class="sd">       ...           5</span></span><a href="#l2526"></a>
<span id="l2527"><span class="sd">       ...</span></span><a href="#l2527"></a>
<span id="l2528"><span class="sd">       ...           And very friendly error messages:</span></span><a href="#l2528"></a>
<span id="l2529"><span class="sd">       ...</span></span><a href="#l2529"></a>
<span id="l2530"><span class="sd">       ...           &gt;&gt;&gt; 1/0</span></span><a href="#l2530"></a>
<span id="l2531"><span class="sd">       ...           To Infinity</span></span><a href="#l2531"></a>
<span id="l2532"><span class="sd">       ...           And</span></span><a href="#l2532"></a>
<span id="l2533"><span class="sd">       ...           Beyond</span></span><a href="#l2533"></a>
<span id="l2534"><span class="sd">       ...</span></span><a href="#l2534"></a>
<span id="l2535"><span class="sd">       ...           You can use logic if you want:</span></span><a href="#l2535"></a>
<span id="l2536"><span class="sd">       ...</span></span><a href="#l2536"></a>
<span id="l2537"><span class="sd">       ...           &gt;&gt;&gt; if 0:</span></span><a href="#l2537"></a>
<span id="l2538"><span class="sd">       ...           ...    blah</span></span><a href="#l2538"></a>
<span id="l2539"><span class="sd">       ...           ...    blah</span></span><a href="#l2539"></a>
<span id="l2540"><span class="sd">       ...           ...</span></span><a href="#l2540"></a>
<span id="l2541"><span class="sd">       ...</span></span><a href="#l2541"></a>
<span id="l2542"><span class="sd">       ...           Ho hum</span></span><a href="#l2542"></a>
<span id="l2543"><span class="sd">       ...           &#39;&#39;&#39;</span></span><a href="#l2543"></a>
<span id="l2544"></span><a href="#l2544"></a>
<span id="l2545"><span class="sd">       &gt;&gt;&gt; print script_from_examples(text)</span></span><a href="#l2545"></a>
<span id="l2546"><span class="sd">       # Here are examples of simple math.</span></span><a href="#l2546"></a>
<span id="l2547"><span class="sd">       #</span></span><a href="#l2547"></a>
<span id="l2548"><span class="sd">       #     Python has super accurate integer addition</span></span><a href="#l2548"></a>
<span id="l2549"><span class="sd">       #</span></span><a href="#l2549"></a>
<span id="l2550"><span class="sd">       2 + 2</span></span><a href="#l2550"></a>
<span id="l2551"><span class="sd">       # Expected:</span></span><a href="#l2551"></a>
<span id="l2552"><span class="sd">       ## 5</span></span><a href="#l2552"></a>
<span id="l2553"><span class="sd">       #</span></span><a href="#l2553"></a>
<span id="l2554"><span class="sd">       #     And very friendly error messages:</span></span><a href="#l2554"></a>
<span id="l2555"><span class="sd">       #</span></span><a href="#l2555"></a>
<span id="l2556"><span class="sd">       1/0</span></span><a href="#l2556"></a>
<span id="l2557"><span class="sd">       # Expected:</span></span><a href="#l2557"></a>
<span id="l2558"><span class="sd">       ## To Infinity</span></span><a href="#l2558"></a>
<span id="l2559"><span class="sd">       ## And</span></span><a href="#l2559"></a>
<span id="l2560"><span class="sd">       ## Beyond</span></span><a href="#l2560"></a>
<span id="l2561"><span class="sd">       #</span></span><a href="#l2561"></a>
<span id="l2562"><span class="sd">       #     You can use logic if you want:</span></span><a href="#l2562"></a>
<span id="l2563"><span class="sd">       #</span></span><a href="#l2563"></a>
<span id="l2564"><span class="sd">       if 0:</span></span><a href="#l2564"></a>
<span id="l2565"><span class="sd">          blah</span></span><a href="#l2565"></a>
<span id="l2566"><span class="sd">          blah</span></span><a href="#l2566"></a>
<span id="l2567"><span class="sd">       #</span></span><a href="#l2567"></a>
<span id="l2568"><span class="sd">       #     Ho hum</span></span><a href="#l2568"></a>
<span id="l2569"><span class="sd">       &lt;BLANKLINE&gt;</span></span><a href="#l2569"></a>
<span id="l2570"><span class="sd">       &quot;&quot;&quot;</span></span><a href="#l2570"></a>
<span id="l2571">    <span class="n">output</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l2571"></a>
<span id="l2572">    <span class="k">for</span> <span class="n">piece</span> <span class="ow">in</span> <span class="n">DocTestParser</span><span class="p">()</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">s</span><span class="p">):</span></span><a href="#l2572"></a>
<span id="l2573">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">piece</span><span class="p">,</span> <span class="n">Example</span><span class="p">):</span></span><a href="#l2573"></a>
<span id="l2574">            <span class="c"># Add the example&#39;s source code (strip trailing NL)</span></span><a href="#l2574"></a>
<span id="l2575">            <span class="n">output</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">piece</span><span class="o">.</span><span class="n">source</span><span class="p">[:</span><span class="o">-</span><span class="mi">1</span><span class="p">])</span></span><a href="#l2575"></a>
<span id="l2576">            <span class="c"># Add the expected output:</span></span><a href="#l2576"></a>
<span id="l2577">            <span class="n">want</span> <span class="o">=</span> <span class="n">piece</span><span class="o">.</span><span class="n">want</span></span><a href="#l2577"></a>
<span id="l2578">            <span class="k">if</span> <span class="n">want</span><span class="p">:</span></span><a href="#l2578"></a>
<span id="l2579">                <span class="n">output</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s">&#39;# Expected:&#39;</span><span class="p">)</span></span><a href="#l2579"></a>
<span id="l2580">                <span class="n">output</span> <span class="o">+=</span> <span class="p">[</span><span class="s">&#39;## &#39;</span><span class="o">+</span><span class="n">l</span> <span class="k">for</span> <span class="n">l</span> <span class="ow">in</span> <span class="n">want</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)[:</span><span class="o">-</span><span class="mi">1</span><span class="p">]]</span></span><a href="#l2580"></a>
<span id="l2581">        <span class="k">else</span><span class="p">:</span></span><a href="#l2581"></a>
<span id="l2582">            <span class="c"># Add non-example text.</span></span><a href="#l2582"></a>
<span id="l2583">            <span class="n">output</span> <span class="o">+=</span> <span class="p">[</span><span class="n">_comment_line</span><span class="p">(</span><span class="n">l</span><span class="p">)</span></span><a href="#l2583"></a>
<span id="l2584">                       <span class="k">for</span> <span class="n">l</span> <span class="ow">in</span> <span class="n">piece</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)[:</span><span class="o">-</span><span class="mi">1</span><span class="p">]]</span></span><a href="#l2584"></a>
<span id="l2585"></span><a href="#l2585"></a>
<span id="l2586">    <span class="c"># Trim junk on both ends.</span></span><a href="#l2586"></a>
<span id="l2587">    <span class="k">while</span> <span class="n">output</span> <span class="ow">and</span> <span class="n">output</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span> <span class="o">==</span> <span class="s">&#39;#&#39;</span><span class="p">:</span></span><a href="#l2587"></a>
<span id="l2588">        <span class="n">output</span><span class="o">.</span><span class="n">pop</span><span class="p">()</span></span><a href="#l2588"></a>
<span id="l2589">    <span class="k">while</span> <span class="n">output</span> <span class="ow">and</span> <span class="n">output</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">==</span> <span class="s">&#39;#&#39;</span><span class="p">:</span></span><a href="#l2589"></a>
<span id="l2590">        <span class="n">output</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span></span><a href="#l2590"></a>
<span id="l2591">    <span class="c"># Combine the output, and return it.</span></span><a href="#l2591"></a>
<span id="l2592">    <span class="c"># Add a courtesy newline to prevent exec from choking (see bug #1172785)</span></span><a href="#l2592"></a>
<span id="l2593">    <span class="k">return</span> <span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">output</span><span class="p">)</span> <span class="o">+</span> <span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span></span><a href="#l2593"></a>
<span id="l2594"></span><a href="#l2594"></a>
<span id="l2595"><span class="k">def</span> <span class="nf">testsource</span><span class="p">(</span><span class="n">module</span><span class="p">,</span> <span class="n">name</span><span class="p">):</span></span><a href="#l2595"></a>
<span id="l2596">    <span class="sd">&quot;&quot;&quot;Extract the test sources from a doctest docstring as a script.</span></span><a href="#l2596"></a>
<span id="l2597"></span><a href="#l2597"></a>
<span id="l2598"><span class="sd">    Provide the module (or dotted name of the module) containing the</span></span><a href="#l2598"></a>
<span id="l2599"><span class="sd">    test to be debugged and the name (within the module) of the object</span></span><a href="#l2599"></a>
<span id="l2600"><span class="sd">    with the doc string with tests to be debugged.</span></span><a href="#l2600"></a>
<span id="l2601"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l2601"></a>
<span id="l2602">    <span class="n">module</span> <span class="o">=</span> <span class="n">_normalize_module</span><span class="p">(</span><span class="n">module</span><span class="p">)</span></span><a href="#l2602"></a>
<span id="l2603">    <span class="n">tests</span> <span class="o">=</span> <span class="n">DocTestFinder</span><span class="p">()</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="n">module</span><span class="p">)</span></span><a href="#l2603"></a>
<span id="l2604">    <span class="n">test</span> <span class="o">=</span> <span class="p">[</span><span class="n">t</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="n">tests</span> <span class="k">if</span> <span class="n">t</span><span class="o">.</span><span class="n">name</span> <span class="o">==</span> <span class="n">name</span><span class="p">]</span></span><a href="#l2604"></a>
<span id="l2605">    <span class="k">if</span> <span class="ow">not</span> <span class="n">test</span><span class="p">:</span></span><a href="#l2605"></a>
<span id="l2606">        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="s">&quot;not found in tests&quot;</span><span class="p">)</span></span><a href="#l2606"></a>
<span id="l2607">    <span class="n">test</span> <span class="o">=</span> <span class="n">test</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span></span><a href="#l2607"></a>
<span id="l2608">    <span class="n">testsrc</span> <span class="o">=</span> <span class="n">script_from_examples</span><span class="p">(</span><span class="n">test</span><span class="o">.</span><span class="n">docstring</span><span class="p">)</span></span><a href="#l2608"></a>
<span id="l2609">    <span class="k">return</span> <span class="n">testsrc</span></span><a href="#l2609"></a>
<span id="l2610"></span><a href="#l2610"></a>
<span id="l2611"><span class="k">def</span> <span class="nf">debug_src</span><span class="p">(</span><span class="n">src</span><span class="p">,</span> <span class="n">pm</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span> <span class="n">globs</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l2611"></a>
<span id="l2612">    <span class="sd">&quot;&quot;&quot;Debug a single doctest docstring, in argument `src`&#39;&quot;&quot;&quot;</span></span><a href="#l2612"></a>
<span id="l2613">    <span class="n">testsrc</span> <span class="o">=</span> <span class="n">script_from_examples</span><span class="p">(</span><span class="n">src</span><span class="p">)</span></span><a href="#l2613"></a>
<span id="l2614">    <span class="n">debug_script</span><span class="p">(</span><span class="n">testsrc</span><span class="p">,</span> <span class="n">pm</span><span class="p">,</span> <span class="n">globs</span><span class="p">)</span></span><a href="#l2614"></a>
<span id="l2615"></span><a href="#l2615"></a>
<span id="l2616"><span class="k">def</span> <span class="nf">debug_script</span><span class="p">(</span><span class="n">src</span><span class="p">,</span> <span class="n">pm</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span> <span class="n">globs</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l2616"></a>
<span id="l2617">    <span class="s">&quot;Debug a test script.  `src` is the script, as a string.&quot;</span></span><a href="#l2617"></a>
<span id="l2618">    <span class="kn">import</span> <span class="nn">pdb</span></span><a href="#l2618"></a>
<span id="l2619"></span><a href="#l2619"></a>
<span id="l2620">    <span class="c"># Note that tempfile.NameTemporaryFile() cannot be used.  As the</span></span><a href="#l2620"></a>
<span id="l2621">    <span class="c"># docs say, a file so created cannot be opened by name a second time</span></span><a href="#l2621"></a>
<span id="l2622">    <span class="c"># on modern Windows boxes, and execfile() needs to open it.</span></span><a href="#l2622"></a>
<span id="l2623">    <span class="n">srcfilename</span> <span class="o">=</span> <span class="n">tempfile</span><span class="o">.</span><span class="n">mktemp</span><span class="p">(</span><span class="s">&quot;.py&quot;</span><span class="p">,</span> <span class="s">&quot;doctestdebug&quot;</span><span class="p">)</span></span><a href="#l2623"></a>
<span id="l2624">    <span class="n">f</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">srcfilename</span><span class="p">,</span> <span class="s">&#39;w&#39;</span><span class="p">)</span></span><a href="#l2624"></a>
<span id="l2625">    <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">src</span><span class="p">)</span></span><a href="#l2625"></a>
<span id="l2626">    <span class="n">f</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></span><a href="#l2626"></a>
<span id="l2627"></span><a href="#l2627"></a>
<span id="l2628">    <span class="k">try</span><span class="p">:</span></span><a href="#l2628"></a>
<span id="l2629">        <span class="k">if</span> <span class="n">globs</span><span class="p">:</span></span><a href="#l2629"></a>
<span id="l2630">            <span class="n">globs</span> <span class="o">=</span> <span class="n">globs</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span></span><a href="#l2630"></a>
<span id="l2631">        <span class="k">else</span><span class="p">:</span></span><a href="#l2631"></a>
<span id="l2632">            <span class="n">globs</span> <span class="o">=</span> <span class="p">{}</span></span><a href="#l2632"></a>
<span id="l2633"></span><a href="#l2633"></a>
<span id="l2634">        <span class="k">if</span> <span class="n">pm</span><span class="p">:</span></span><a href="#l2634"></a>
<span id="l2635">            <span class="k">try</span><span class="p">:</span></span><a href="#l2635"></a>
<span id="l2636">                <span class="nb">execfile</span><span class="p">(</span><span class="n">srcfilename</span><span class="p">,</span> <span class="n">globs</span><span class="p">,</span> <span class="n">globs</span><span class="p">)</span></span><a href="#l2636"></a>
<span id="l2637">            <span class="k">except</span><span class="p">:</span></span><a href="#l2637"></a>
<span id="l2638">                <span class="k">print</span> <span class="n">sys</span><span class="o">.</span><span class="n">exc_info</span><span class="p">()[</span><span class="mi">1</span><span class="p">]</span></span><a href="#l2638"></a>
<span id="l2639">                <span class="n">pdb</span><span class="o">.</span><span class="n">post_mortem</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">exc_info</span><span class="p">()[</span><span class="mi">2</span><span class="p">])</span></span><a href="#l2639"></a>
<span id="l2640">        <span class="k">else</span><span class="p">:</span></span><a href="#l2640"></a>
<span id="l2641">            <span class="c"># Note that %r is vital here.  &#39;%s&#39; instead can, e.g., cause</span></span><a href="#l2641"></a>
<span id="l2642">            <span class="c"># backslashes to get treated as metacharacters on Windows.</span></span><a href="#l2642"></a>
<span id="l2643">            <span class="n">pdb</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="s">&quot;execfile(</span><span class="si">%r</span><span class="s">)&quot;</span> <span class="o">%</span> <span class="n">srcfilename</span><span class="p">,</span> <span class="n">globs</span><span class="p">,</span> <span class="n">globs</span><span class="p">)</span></span><a href="#l2643"></a>
<span id="l2644"></span><a href="#l2644"></a>
<span id="l2645">    <span class="k">finally</span><span class="p">:</span></span><a href="#l2645"></a>
<span id="l2646">        <span class="n">os</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">srcfilename</span><span class="p">)</span></span><a href="#l2646"></a>
<span id="l2647"></span><a href="#l2647"></a>
<span id="l2648"><span class="k">def</span> <span class="nf">debug</span><span class="p">(</span><span class="n">module</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">pm</span><span class="o">=</span><span class="bp">False</span><span class="p">):</span></span><a href="#l2648"></a>
<span id="l2649">    <span class="sd">&quot;&quot;&quot;Debug a single doctest docstring.</span></span><a href="#l2649"></a>
<span id="l2650"></span><a href="#l2650"></a>
<span id="l2651"><span class="sd">    Provide the module (or dotted name of the module) containing the</span></span><a href="#l2651"></a>
<span id="l2652"><span class="sd">    test to be debugged and the name (within the module) of the object</span></span><a href="#l2652"></a>
<span id="l2653"><span class="sd">    with the docstring with tests to be debugged.</span></span><a href="#l2653"></a>
<span id="l2654"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l2654"></a>
<span id="l2655">    <span class="n">module</span> <span class="o">=</span> <span class="n">_normalize_module</span><span class="p">(</span><span class="n">module</span><span class="p">)</span></span><a href="#l2655"></a>
<span id="l2656">    <span class="n">testsrc</span> <span class="o">=</span> <span class="n">testsource</span><span class="p">(</span><span class="n">module</span><span class="p">,</span> <span class="n">name</span><span class="p">)</span></span><a href="#l2656"></a>
<span id="l2657">    <span class="n">debug_script</span><span class="p">(</span><span class="n">testsrc</span><span class="p">,</span> <span class="n">pm</span><span class="p">,</span> <span class="n">module</span><span class="o">.</span><span class="n">__dict__</span><span class="p">)</span></span><a href="#l2657"></a>
<span id="l2658"></span><a href="#l2658"></a>
<span id="l2659"><span class="c">######################################################################</span></span><a href="#l2659"></a>
<span id="l2660"><span class="c">## 10. Example Usage</span></span><a href="#l2660"></a>
<span id="l2661"><span class="c">######################################################################</span></span><a href="#l2661"></a>
<span id="l2662"><span class="k">class</span> <span class="nc">_TestClass</span><span class="p">:</span></span><a href="#l2662"></a>
<span id="l2663">    <span class="sd">&quot;&quot;&quot;</span></span><a href="#l2663"></a>
<span id="l2664"><span class="sd">    A pointless class, for sanity-checking of docstring testing.</span></span><a href="#l2664"></a>
<span id="l2665"></span><a href="#l2665"></a>
<span id="l2666"><span class="sd">    Methods:</span></span><a href="#l2666"></a>
<span id="l2667"><span class="sd">        square()</span></span><a href="#l2667"></a>
<span id="l2668"><span class="sd">        get()</span></span><a href="#l2668"></a>
<span id="l2669"></span><a href="#l2669"></a>
<span id="l2670"><span class="sd">    &gt;&gt;&gt; _TestClass(13).get() + _TestClass(-12).get()</span></span><a href="#l2670"></a>
<span id="l2671"><span class="sd">    1</span></span><a href="#l2671"></a>
<span id="l2672"><span class="sd">    &gt;&gt;&gt; hex(_TestClass(13).square().get())</span></span><a href="#l2672"></a>
<span id="l2673"><span class="sd">    &#39;0xa9&#39;</span></span><a href="#l2673"></a>
<span id="l2674"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l2674"></a>
<span id="l2675"></span><a href="#l2675"></a>
<span id="l2676">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">val</span><span class="p">):</span></span><a href="#l2676"></a>
<span id="l2677">        <span class="sd">&quot;&quot;&quot;val -&gt; _TestClass object with associated value val.</span></span><a href="#l2677"></a>
<span id="l2678"></span><a href="#l2678"></a>
<span id="l2679"><span class="sd">        &gt;&gt;&gt; t = _TestClass(123)</span></span><a href="#l2679"></a>
<span id="l2680"><span class="sd">        &gt;&gt;&gt; print t.get()</span></span><a href="#l2680"></a>
<span id="l2681"><span class="sd">        123</span></span><a href="#l2681"></a>
<span id="l2682"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l2682"></a>
<span id="l2683"></span><a href="#l2683"></a>
<span id="l2684">        <span class="bp">self</span><span class="o">.</span><span class="n">val</span> <span class="o">=</span> <span class="n">val</span></span><a href="#l2684"></a>
<span id="l2685"></span><a href="#l2685"></a>
<span id="l2686">    <span class="k">def</span> <span class="nf">square</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l2686"></a>
<span id="l2687">        <span class="sd">&quot;&quot;&quot;square() -&gt; square TestClass&#39;s associated value</span></span><a href="#l2687"></a>
<span id="l2688"></span><a href="#l2688"></a>
<span id="l2689"><span class="sd">        &gt;&gt;&gt; _TestClass(13).square().get()</span></span><a href="#l2689"></a>
<span id="l2690"><span class="sd">        169</span></span><a href="#l2690"></a>
<span id="l2691"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l2691"></a>
<span id="l2692"></span><a href="#l2692"></a>
<span id="l2693">        <span class="bp">self</span><span class="o">.</span><span class="n">val</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">val</span> <span class="o">**</span> <span class="mi">2</span></span><a href="#l2693"></a>
<span id="l2694">        <span class="k">return</span> <span class="bp">self</span></span><a href="#l2694"></a>
<span id="l2695"></span><a href="#l2695"></a>
<span id="l2696">    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l2696"></a>
<span id="l2697">        <span class="sd">&quot;&quot;&quot;get() -&gt; return TestClass&#39;s associated value.</span></span><a href="#l2697"></a>
<span id="l2698"></span><a href="#l2698"></a>
<span id="l2699"><span class="sd">        &gt;&gt;&gt; x = _TestClass(-42)</span></span><a href="#l2699"></a>
<span id="l2700"><span class="sd">        &gt;&gt;&gt; print x.get()</span></span><a href="#l2700"></a>
<span id="l2701"><span class="sd">        -42</span></span><a href="#l2701"></a>
<span id="l2702"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l2702"></a>
<span id="l2703"></span><a href="#l2703"></a>
<span id="l2704">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">val</span></span><a href="#l2704"></a>
<span id="l2705"></span><a href="#l2705"></a>
<span id="l2706"><span class="n">__test__</span> <span class="o">=</span> <span class="p">{</span><span class="s">&quot;_TestClass&quot;</span><span class="p">:</span> <span class="n">_TestClass</span><span class="p">,</span></span><a href="#l2706"></a>
<span id="l2707">            <span class="s">&quot;string&quot;</span><span class="p">:</span> <span class="s">r&quot;&quot;&quot;</span></span><a href="#l2707"></a>
<span id="l2708"><span class="s">                      Example of a string object, searched as-is.</span></span><a href="#l2708"></a>
<span id="l2709"><span class="s">                      &gt;&gt;&gt; x = 1; y = 2</span></span><a href="#l2709"></a>
<span id="l2710"><span class="s">                      &gt;&gt;&gt; x + y, x * y</span></span><a href="#l2710"></a>
<span id="l2711"><span class="s">                      (3, 2)</span></span><a href="#l2711"></a>
<span id="l2712"><span class="s">                      &quot;&quot;&quot;</span><span class="p">,</span></span><a href="#l2712"></a>
<span id="l2713"></span><a href="#l2713"></a>
<span id="l2714">            <span class="s">&quot;bool-int equivalence&quot;</span><span class="p">:</span> <span class="s">r&quot;&quot;&quot;</span></span><a href="#l2714"></a>
<span id="l2715"><span class="s">                                    In 2.2, boolean expressions displayed</span></span><a href="#l2715"></a>
<span id="l2716"><span class="s">                                    0 or 1.  By default, we still accept</span></span><a href="#l2716"></a>
<span id="l2717"><span class="s">                                    them.  This can be disabled by passing</span></span><a href="#l2717"></a>
<span id="l2718"><span class="s">                                    DONT_ACCEPT_TRUE_FOR_1 to the new</span></span><a href="#l2718"></a>
<span id="l2719"><span class="s">                                    optionflags argument.</span></span><a href="#l2719"></a>
<span id="l2720"><span class="s">                                    &gt;&gt;&gt; 4 == 4</span></span><a href="#l2720"></a>
<span id="l2721"><span class="s">                                    1</span></span><a href="#l2721"></a>
<span id="l2722"><span class="s">                                    &gt;&gt;&gt; 4 == 4</span></span><a href="#l2722"></a>
<span id="l2723"><span class="s">                                    True</span></span><a href="#l2723"></a>
<span id="l2724"><span class="s">                                    &gt;&gt;&gt; 4 &gt; 4</span></span><a href="#l2724"></a>
<span id="l2725"><span class="s">                                    0</span></span><a href="#l2725"></a>
<span id="l2726"><span class="s">                                    &gt;&gt;&gt; 4 &gt; 4</span></span><a href="#l2726"></a>
<span id="l2727"><span class="s">                                    False</span></span><a href="#l2727"></a>
<span id="l2728"><span class="s">                                    &quot;&quot;&quot;</span><span class="p">,</span></span><a href="#l2728"></a>
<span id="l2729"></span><a href="#l2729"></a>
<span id="l2730">            <span class="s">&quot;blank lines&quot;</span><span class="p">:</span> <span class="s">r&quot;&quot;&quot;</span></span><a href="#l2730"></a>
<span id="l2731"><span class="s">                Blank lines can be marked with &lt;BLANKLINE&gt;:</span></span><a href="#l2731"></a>
<span id="l2732"><span class="s">                    &gt;&gt;&gt; print &#39;foo\n\nbar\n&#39;</span></span><a href="#l2732"></a>
<span id="l2733"><span class="s">                    foo</span></span><a href="#l2733"></a>
<span id="l2734"><span class="s">                    &lt;BLANKLINE&gt;</span></span><a href="#l2734"></a>
<span id="l2735"><span class="s">                    bar</span></span><a href="#l2735"></a>
<span id="l2736"><span class="s">                    &lt;BLANKLINE&gt;</span></span><a href="#l2736"></a>
<span id="l2737"><span class="s">            &quot;&quot;&quot;</span><span class="p">,</span></span><a href="#l2737"></a>
<span id="l2738"></span><a href="#l2738"></a>
<span id="l2739">            <span class="s">&quot;ellipsis&quot;</span><span class="p">:</span> <span class="s">r&quot;&quot;&quot;</span></span><a href="#l2739"></a>
<span id="l2740"><span class="s">                If the ellipsis flag is used, then &#39;...&#39; can be used to</span></span><a href="#l2740"></a>
<span id="l2741"><span class="s">                elide substrings in the desired output:</span></span><a href="#l2741"></a>
<span id="l2742"><span class="s">                    &gt;&gt;&gt; print range(1000) #doctest: +ELLIPSIS</span></span><a href="#l2742"></a>
<span id="l2743"><span class="s">                    [0, 1, 2, ..., 999]</span></span><a href="#l2743"></a>
<span id="l2744"><span class="s">            &quot;&quot;&quot;</span><span class="p">,</span></span><a href="#l2744"></a>
<span id="l2745"></span><a href="#l2745"></a>
<span id="l2746">            <span class="s">&quot;whitespace normalization&quot;</span><span class="p">:</span> <span class="s">r&quot;&quot;&quot;</span></span><a href="#l2746"></a>
<span id="l2747"><span class="s">                If the whitespace normalization flag is used, then</span></span><a href="#l2747"></a>
<span id="l2748"><span class="s">                differences in whitespace are ignored.</span></span><a href="#l2748"></a>
<span id="l2749"><span class="s">                    &gt;&gt;&gt; print range(30) #doctest: +NORMALIZE_WHITESPACE</span></span><a href="#l2749"></a>
<span id="l2750"><span class="s">                    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,</span></span><a href="#l2750"></a>
<span id="l2751"><span class="s">                     15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,</span></span><a href="#l2751"></a>
<span id="l2752"><span class="s">                     27, 28, 29]</span></span><a href="#l2752"></a>
<span id="l2753"><span class="s">            &quot;&quot;&quot;</span><span class="p">,</span></span><a href="#l2753"></a>
<span id="l2754">           <span class="p">}</span></span><a href="#l2754"></a>
<span id="l2755"></span><a href="#l2755"></a>
<span id="l2756"></span><a href="#l2756"></a>
<span id="l2757"><span class="k">def</span> <span class="nf">_test</span><span class="p">():</span></span><a href="#l2757"></a>
<span id="l2758">    <span class="n">testfiles</span> <span class="o">=</span> <span class="p">[</span><span class="n">arg</span> <span class="k">for</span> <span class="n">arg</span> <span class="ow">in</span> <span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span> <span class="k">if</span> <span class="n">arg</span> <span class="ow">and</span> <span class="n">arg</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">!=</span> <span class="s">&#39;-&#39;</span><span class="p">]</span></span><a href="#l2758"></a>
<span id="l2759">    <span class="k">if</span> <span class="ow">not</span> <span class="n">testfiles</span><span class="p">:</span></span><a href="#l2759"></a>
<span id="l2760">        <span class="n">name</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">basename</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span></span><a href="#l2760"></a>
<span id="l2761">        <span class="k">if</span> <span class="s">&#39;__loader__&#39;</span> <span class="ow">in</span> <span class="nb">globals</span><span class="p">():</span>          <span class="c"># python -m</span></span><a href="#l2761"></a>
<span id="l2762">            <span class="n">name</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">splitext</span><span class="p">(</span><span class="n">name</span><span class="p">)</span></span><a href="#l2762"></a>
<span id="l2763">        <span class="k">print</span><span class="p">(</span><span class="s">&quot;usage: {0} [-v] file ...&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">name</span><span class="p">))</span></span><a href="#l2763"></a>
<span id="l2764">        <span class="k">return</span> <span class="mi">2</span></span><a href="#l2764"></a>
<span id="l2765">    <span class="k">for</span> <span class="n">filename</span> <span class="ow">in</span> <span class="n">testfiles</span><span class="p">:</span></span><a href="#l2765"></a>
<span id="l2766">        <span class="k">if</span> <span class="n">filename</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s">&quot;.py&quot;</span><span class="p">):</span></span><a href="#l2766"></a>
<span id="l2767">            <span class="c"># It is a module -- insert its dir into sys.path and try to</span></span><a href="#l2767"></a>
<span id="l2768">            <span class="c"># import it. If it is part of a package, that possibly</span></span><a href="#l2768"></a>
<span id="l2769">            <span class="c"># won&#39;t work because of package imports.</span></span><a href="#l2769"></a>
<span id="l2770">            <span class="n">dirname</span><span class="p">,</span> <span class="n">filename</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">filename</span><span class="p">)</span></span><a href="#l2770"></a>
<span id="l2771">            <span class="n">sys</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">dirname</span><span class="p">)</span></span><a href="#l2771"></a>
<span id="l2772">            <span class="n">m</span> <span class="o">=</span> <span class="nb">__import__</span><span class="p">(</span><span class="n">filename</span><span class="p">[:</span><span class="o">-</span><span class="mi">3</span><span class="p">])</span></span><a href="#l2772"></a>
<span id="l2773">            <span class="k">del</span> <span class="n">sys</span><span class="o">.</span><span class="n">path</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span></span><a href="#l2773"></a>
<span id="l2774">            <span class="n">failures</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="n">testmod</span><span class="p">(</span><span class="n">m</span><span class="p">)</span></span><a href="#l2774"></a>
<span id="l2775">        <span class="k">else</span><span class="p">:</span></span><a href="#l2775"></a>
<span id="l2776">            <span class="n">failures</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="n">testfile</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="n">module_relative</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span></span><a href="#l2776"></a>
<span id="l2777">        <span class="k">if</span> <span class="n">failures</span><span class="p">:</span></span><a href="#l2777"></a>
<span id="l2778">            <span class="k">return</span> <span class="mi">1</span></span><a href="#l2778"></a>
<span id="l2779">    <span class="k">return</span> <span class="mi">0</span></span><a href="#l2779"></a>
<span id="l2780"></span><a href="#l2780"></a>
<span id="l2781"></span><a href="#l2781"></a>
<span id="l2782"><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&quot;__main__&quot;</span><span class="p">:</span></span><a href="#l2782"></a>
<span id="l2783">    <span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="n">_test</span><span class="p">())</span></span><a href="#l2783"></a></pre>
<div class="sourcelast"></div>
</div>
</div>
</div>

<script type="text/javascript">process_dates()</script>


</body>
</html>

